import boto3

def check_imdsv2_status(region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)

    response = ec2.describe_instances()
    non_compliant_instances = []
    compliant_instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            metadata_options = instance.get('MetadataOptions', {})

            if metadata_options.get('HttpTokens') == 'required':
                print(f"[OK] {instance_id} has IMDSv2 enforced.")
                compliant_instances.append(instance_id)
            else:
                print(f"[WARNING] {instance_id} does NOT have IMDSv2 enforced.")
                non_compliant_instances.append(instance_id)

    print("\nSummary:")
    print(f"✔️ Compliant Instances: {len(compliant_instances)}")
    print(f"❌ Non-Compliant Instances: {len(non_compliant_instances)}")
    if non_compliant_instances:
        print("List of non-compliant instances:")
        for i in non_compliant_instances:
            print(f" - {i}")

if __name__ == "__main__":
    check_imdsv2_status(region='us-east-1')  # Change region as needed
