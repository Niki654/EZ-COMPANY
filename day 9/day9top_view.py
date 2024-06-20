# class node:
#     def __init__(self,data):
#         self.value=data
#         self.left=None
#         self.right=None
# class node_data:
#     def __init__(self,node,hkey) -> None:
#         self.node=node
#         self.hkey=hkey
# def top_view(root):
#     temp=node_data(root,0)
#     q=[temp]
#     q.append(None)
    
#     key_dict={}
#     while len(q)!=0:  
#         curr=q.pop(0)  
        
#         if curr==None:
#             if len(q)==0:
#                 break
#             else:
#                 q.append(None)
#         else:
#             if curr.hkey not in key_dict.keys():
#                 key_dict[curr.hkey]=curr.node.value
                
#             if curr.node.left!=None:
#                 temp=node_data(curr.node.left,curr.hkey-1)
#                 q.append(temp)
#             if curr.node.right!=None:
#                 temp=node_data(curr.node.right,curr.hkey+1)
#                 q.append(temp)        
#     for i in sorted(key_dict):
#         print(key_dict[i],end=' ')
#     print(key_dict)
     
# if __name__=="__main__":  
#     root = node(1)

#     root.left=node(2)    
#     root.right=node(3)
    
#     root.left.left=node(4)
#     root.left.right=node(5)
    
#     root.right.left=node(6)
#     root.right.right=node(7)
    
#     root.left.right.left=node(9) 
#     root.left.right.right=node(10)
#     root.right.right.right=node(11)
#     root.left.right.left.left=node(12)
#     root.left.right.left.right=node(13)  
# top_view(root)   
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class node_data:
    def __init__(self,node,hkey) -> None:
        self.node=node
        self.hkey=hkey
def top_view(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)
    
    key_dict={}
    while len(q)!=0:  
        curr=q.pop(0)  
        
        if curr==None:
            if len(q)==0:
                break
            else:
                # print(q[0].value)
                q.append(None)          
        else:
            if curr.hkey not in key_dict.keys():
                key_dict[curr.hkey]=curr.node.value
                
            if curr.node.left!=None:
                temp=node_data(curr.node.left,curr.hkey-1)
                q.append(temp)
            if curr.node.right!=None:
                temp=node_data(curr.node.right,curr.hkey+1)
                q.append(temp)        
    for i in sorted(key_dict):
        print(key_dict[i],end=' ')
    print(key_dict)
     
if __name__=="__main__":  
    root = node(1)

    root.left=node(2)    
    root.right=node(3)
    
    root.left.left=node(4)
    root.left.right=node(5)
    
    root.right.left=node(6)
    root.right.right=node(7)
    
    root.left.right.left=node(9) 
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)  
top_view(root)             