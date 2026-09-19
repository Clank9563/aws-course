import boto3

def main():
    sts = boto3.client("sts")

    response = sts.get_caller_identity()

    print("AWS boto3 測試成功！")
    print(f"Account : {response['Account']}")
    print(f"UserId  : {response['UserId']}")
    print(f"ARN     : {response['Arn']}")


if __name__ == "__main__":
    main()