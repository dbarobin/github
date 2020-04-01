#!/bin/bash

# This script is used to do a cron job to refresh github host at /etc/hosts every hour

BASE_PATH=$(dirname $(readlink -f $0))
GITHUB_HOST_PATH="/usr/lib/github_host"
ROOT_CRON_FILE="/var/spool/cron/root"

rm -rf $GITHUB_HOST_PATH && rm -rf /usr/bin/github_host

mkdir -p $GITHUB_HOST_PATH

cp ${BASE_PATH}/../github* ${GITHUB_HOST_PATH}/
cp ${BASE_PATH}/linux_run.sh ${GITHUB_HOST_PATH}/

ln -s ${GITHUB_HOST_PATH}/linux_run.sh /usr/bin/github_host
chmod 0500 /usr/bin/github_host

# Add github host first
/usr/bin/github_host

# Add cron job for user root
if [ ! -e /var/spool/cron/root ] || ! cat $ROOT_CRON_FILE | grep "github_host" > /dev/null; then
    echo "0 * * * * /usr/bin/github_host" >> $ROOT_CRON_FILE

    # Restart crond service
    systemctl restart crond
fi