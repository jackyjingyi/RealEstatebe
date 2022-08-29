from obs import ObsClient

obsClient = ObsClient(
    access_key_id='IUGZAGPF5UACEBEZEQJA',
    security_token='lLcJyV4y6ujOmbdTkDdz64R9oBY3pr19ewTY081N',
    server='https://obs.cn-south-1.myhuaweicloud.com'
)

bucket = obsClient.listObjects('oct-project-collection','/')
# resp = bucket.listObjects('/')
print(bucket)