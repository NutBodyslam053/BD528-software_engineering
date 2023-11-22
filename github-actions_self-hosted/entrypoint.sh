#!/bin/bash

### Create a GitHub registration token for a repository
# "https://docs.github.com/rest/actions/self-hosted-runners#create-a-registration-token-for-a-repository"

PAYLOAD=$(
curl -L \
    -X POST \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer ${GITHUB_TOKEN}" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/repos/${GITHUB_USER}/${GITHUB_REPOSITORY}/actions/runners/registration-token
)
echo ${PAYLOAD}

RUNNER_TOKEN=$(echo ${PAYLOAD} | jq .token --raw-output)
echo ${RUNNER_TOKEN}

./config.sh \
    --unattended \
    --url https://github.com/${GITHUB_USER}/${GITHUB_REPOSITORY} \
    --token ${RUNNER_TOKEN} \
    --replace \
    --name ${HOSTNAME} \
    --labels my-runner

remove() {
    ./config.sh remove --token "${RUNNER_TOKEN}"
}

trap 'remove; exit 130' INT
trap 'remove; exit 143' TERM

./run.sh "$*" &

wait $!
