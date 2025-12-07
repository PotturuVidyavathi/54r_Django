# class basicMiddleware:
#     def __init__(self,get_response):      # when server starts __init__() function excetues --> used to create a object of middleware
#         self.get_response=get_response

#     def __call__(self,request):       #whenever we make a request this __call__() function executes  --> helps to get the request 
#         print(request,"hello")
#         if(request.path=="/student"):
#             print(request.method,"method")
#             print(request.path)
#         response = self.get_response(request)
#         return response

