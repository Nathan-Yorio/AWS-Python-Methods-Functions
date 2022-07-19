import boto3

# Choose either alb or elb, otherwise fail
def app_load_balancers():
    elb = boto3.client('elbv2')                    # set the boto3 client to application load balancers to v2
    top_level_response = 'LoadBalancers'           # Comes from V2 describe_load_balancers Response Syntax

    balancer_name = elb.describe_load_balancers()

    #Grab the load balancer named from each
    #return syntax block
    temp_list = []
    for i in balancer_name[top_level_response]:    # Go inside of each returned syntax block
        temp_list.append(i['LoadBalancerName'])    # Retrieve the Load Balancer's Name and add to list
    return temp_list                               # Function gives us the list


######## Debug #########
""" new_list=app_load_balancers()

# Raw array
print (new_list)

# Array line by line
for x in new_list:
    print(x) """
########################
