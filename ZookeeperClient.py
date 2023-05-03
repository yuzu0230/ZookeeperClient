from kazoo.client import KazooClient
from kazoo.exceptions import NodeExistsError, NoNodeError


class ZookeeperClient:
    def __init__(self, ip, port):
        self.zkClient = KazooClient(hosts=str(ip)+':'+str(port))
        self.zkClient.start()

    def createNode(self, path, value):
        try:
            # Create a node with data
            self.zkClient.create(path=path, value=str(value).encode())
            print(f"Successfully create at {path} with value {value}")
        except NodeExistsError:
            print(f"This node has already existed at path {path}")
        except NoNodeError:
            print(f"Please check all the node exists at path {path}")

    def getData(self, path):
        # Determine if a node exists
        if self.zkClient.exists(path):
            # Print the version of a node and its data
            data, stat = self.zkClient.get(path)
            print(
                f"Path: {path}, Version: {stat.version}, data: {data.decode('utf-8')}")
        else:
            print(f"No node exists at path {str(path)}")

    def getChildNode(self, path):
        # Determine if a node exists
        if self.zkClient.exists(path):
            # List the children
            children = self.zkClient.get_children(path)
            print(
                f"There are {len(children)} children with names {children} at path {path}")
        else:
            print(f"No node exists at path {str(path)}")

    def updateData(self, path, value):
        # Determine if a node exists
        if self.zkClient.exists(path):
            self.zkClient.set(path, str(value).encode())
            print(f"Successfully update at path {path} with value {value}")
        else:
            print(f"No node exists at path {str(path)}")

    def deleteNode(self, path, recursive=True):
        # Determine if a node exists
        if self.zkClient.exists(path):
            # Deletes a node, if recursive is True, can recursively delete all children of node
            self.zkClient.delete(path, recursive=recursive)
            print(f"Successfully delete node and children node at path {path}")
        else:
            print(f"No node exists at path {str(path)}")

    def dropConnection(self):
        self.zkClient.stop()


if __name__ == "__main__":
    zkClient = ZookeeperClient(ip="127.0.0.1", port="2181")
    # Test create function
    zkClient.createNode("/test", "HelloWorld")
    zkClient.createNode("/test/child", "I am the child of test")
    # Test read function
    zkClient.getData("/test")
    zkClient.getChildNode("/test")
    # Test update function
    zkClient.updateData("/test", "hi")
    zkClient.getData("/test")
    # Test delete function
    zkClient.deleteNode("/test")
    zkClient.getData("/test")
    zkClient.getChildNode("/test")
    # Drop connection
    zkClient.dropConnection()
