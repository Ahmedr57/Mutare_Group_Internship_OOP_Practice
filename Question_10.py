# Implement a class ResourceHandler that manages a resource (like a file or a network connection). 
# Use a constructor to allocate the resource and a destructor (__del__ method) to release it. 
# Demonstrate how Python's garbage collection handles object destruction when multiple ResourceHandler 
# objects are created and deleted in different scopes. 
# Also, explain the potential memory management issues that could arise if destructors are not properly used

class ResourceHandler:
    def __init__(self, resource_name):
        self.resource_name = resource_name
        print(f"Allocating Resources: {resource_name}")

    def __del__(self):
        print(f"Releasing Resources: {self.resource_name}")


def exp_func():
    resource1 = ResourceHandler("Resource 1")
    print("Inside the function.....")     

resource2 = ResourceHandler("Resource 2")
exp_func()
resource3 = ResourceHandler("Resource 3")
resource4 = ResourceHandler("Resource 4")