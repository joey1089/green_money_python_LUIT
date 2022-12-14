#Create a AWS Service Inventory List
# 1. The list should be empty initially.
# 2. Populate the list using append or insert.
# 3. Print the list and the length of the list.
# 4. Remove two specific services from the list by name or by index.
# 5. Print the new list and the new length of the list.

aws_list_items = []
aws_list_items.append('RDS')
aws_list_items.append('S3')
aws_list_items.append('Lambda')
aws_list_items.append('EC2')
aws_list_items.append('DynamoDB')
aws_list_items.append('Cloud9')
aws_list_items.append('Kinesis')
aws_list_items.append('DocumentDB')

# Conversion of List to String
str_aws_list = " "
print('AWS Service list:',str_aws_list,','.join(aws_list_items)) # using join to print it as a string items.

# Print the total list item and its list
print(f"AWS Service listed here is around {len(aws_list_items)} and they are \n {aws_list_items} ")

# Removing Cloud9 and DocumentDB from the aws_list_items
aws_list_items.pop(5)
aws_list_items.pop(len(aws_list_items)-1) #using len(list)-1 to find the last element in the list.

# Printing the list after the removal of 2 items.
print(f"After removing few AWS Service, new list is around {len(aws_list_items)} and they are \n {aws_list_items} ")
