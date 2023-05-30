from django.shortcuts import render
from django.db.models import Sum
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Log,brookuser,complaint, product, cart, category, Review, order, payment, order_price
from brookwoodapp.serializers import LoginUserSerializer,ComplaintSerializer, UserRegisterSerializer, ProductSerializer, CartSerializer, categorySerializer, ComplaintSerializer, ReviewSerializer, OrderSerializer, PaymentSerializer, OrderPriceSerializer

# Create your views here.


class UserRegisterSerializeraAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    serializer_class_login = LoginUserSerializer

    def post(self, request):

        login_id=''
        fullname = request.data.get('fullname')
        housename = request.data.get('housename')
        roadname = request.data.get('roadname')
        city = request.data.get('city')
        state = request.data.get('state')
        post = request.data.get('post')
        pincode = request.data.get('pincode')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        username = request.data.get('username')
        userpassword = request.data.get('userpassword')
        role = 'brookuser'
        userstatus = '0'

        if(Log.objects.filter(username=username)):
            return Response({'message': 'Duplicate Username Found'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data = {'username':username,'password':userpassword,'role':role})

        if serializer_login.is_valid():
            log = serializer_login.save()
            login_id = log.id
            print(login_id)
        serializer = self.serializer_class(data= {'fullname':fullname,'housename':housename,'roadname':roadname,'city':city,'state':state,'post':post,'pincode':pincode,'email':email,'phone_number':phone_number,'log_id':login_id,'userstatus':userstatus,'role':role})
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'User registered successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(GenericAPIView):
    serializer_class = LoginUserSerializer
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        logreg = Log.objects.filter(username=username, password = password)
        if(logreg.count()>0):
            read_serializer  = LoginUserSerializer(logreg, many=True)
            for i in read_serializer.data:
                id = i['id']
                print(id)
                role = i['role']
                regdata=brookuser.objects.all().filter(log_id=id).values()
                print(regdata)
                for i in regdata:
                     u_id = i['id']
                     l_status=i['userstatus']
                     f_name=i['fullname']
                     print(u_id)
                
            return Response({'data':{'login_id':id,'username':username,'password':password,'role':role,'user_id':u_id,'l_status':l_status,'name':f_name},'success': True, 'message':'Logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'username or password is invalid','success':False,}, status = status.HTTP_400_BAD_REQUEST)



class SingleUserAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = brookuser.objects.get(pk=id)
        serializer =UserRegisterSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single user data', 'success':True}, status=status.HTTP_200_OK)



class Update_UserAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def put(self, request, id):
        queryset = brookuser.objects.get(pk=id)
        print(queryset)
        serializer = UserRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something Went Wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class ComplaintAPIView(GenericAPIView):
    serializer_class = ComplaintSerializer

    def post(self, request):
        user = request.data.get('user')
        product=request.data.get('product')
        complaint = request.data.get('complaint')
        date = request.data.get('date')
        complaint_status="0"

        serializer = self.serializer_class(data= {'user':user,'complaint':complaint,'product':product,'date':date,'complaint_status':complaint_status})
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'complaint added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)



class ComplaintSingleAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = brookuser.objects.all().filter(pk=id).values()
        print(queryset)
        for i in queryset:
            user = i['id']
            print('///////////',user)
        instance = complaint.objects.all().filter(user=user).values()
        print("======",instance)
        # serializer = ComplaintSerializer(instance)
        return Response({'data': instance, 'message':'complaint  data', 'success':True}, status=status.HTTP_200_OK)




class Get_ProductAPIView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self, request):
        queryset = product.objects.all()
        if (queryset.count()>0):
            serializer = ProductSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'product all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleProductAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = product.objects.get(pk=id)
        serializer =ProductSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single product data', 'success':True}, status=status.HTTP_200_OK)



class CartAPIView(GenericAPIView):
    serializer_class = CartSerializer

    def post(self, request):
        total_price=""
        image=""
        category=""
        p_status=""
        prices=""

        
        user = request.data.get('user')
        products=request.data.get('product')
        print(product)
        quty = request.data.get('quantity')
        quantity=int(quty)
        cart_status="0"
        
        carts = cart.objects.filter(user=user, product=products)
        if carts.exists():
            return Response({'message':'Item is already in cart','success':False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            data=product.objects.all().filter(id=products).values()
            for i in data:
                print(i)
                prices=i['product_price']
                p_status=i['product_status']
                ctgry=i['category_id']
                p_name=i['product_name']
                print(ctgry)
                price=int(prices)
                print(price)
                total_price=price*quantity
                print(total_price)
                tp=str(total_price)

            producto = product.objects.get(id=products)
            product_image = producto.image
            print(image)
                

            serializer = self.serializer_class(data= {'user':user,'product':products,'quantity':quantity,'total_price':tp,'cart_status':cart_status,'category':ctgry,'image':product_image,'p_name':p_name})
            print(serializer)
            if serializer.is_valid():
                print("hi")
                serializer.save()
                return Response({'data':serializer.data,'message':'cart added successfully', 'success':True}, status = status.HTTP_201_CREATED)
            return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)



class SingleCartAPIView(GenericAPIView):
    
    def get(self, request, id):
        # u_id=""
        # qset = brookuser.objects.all().filter(pk=id).values()
        # for i in qset:
        #     u_id=i['id']

        # data=cart.objects.all().filter(user=u_id).values()
        # u_id = brookuser.objects.get(pk=id).id
        # data = cart.objects.filter(user=u_id)
        # print(data)
        # serializer =CartSerializer(data)
        u_id=""
        qset = brookuser.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']

        data = cart.objects.filter(user=u_id).values()
        serialized_data = list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['image'] = settings.MEDIA_URL + str(obj['image'])
        return Response({'data':serialized_data, 'message':'single product data', 'success':True}, status=status.HTTP_200_OK)




class CartIncrementQuantityAPIView(GenericAPIView):
    
    def put(self, request, id):
        cart_item = cart.objects.get(pk=id)

        qnty=cart_item.quantity 
        qty=int(qnty)

        cart_item.quantity=qty + 1

        q=cart_item.quantity
        qn=int(q)

        pr=cart_item.product.product_price
        price=int(pr)

        tp=price*qn
        cart_item.total_price=tp
        
        cart_item.save()
        serialized_data = CartSerializer(cart_item, context={'request': request}).data
        serialized_data['image'] = str(serialized_data['image']).split('http://localhost:8000')[1]
        # for obj in serialized_data:
        #     obj['image'] = settings.MEDIA_URL + str(obj['image'])
        return Response({'data': serialized_data, 'message': 'Cart item quantity updated', 'success': True}, status=status.HTTP_200_OK)


class CartDecrementQuantityAPIView(GenericAPIView):
    
    def put(self, request, id):
        cart_item = cart.objects.get(pk=id)
        qny=cart_item.quantity
        qant=int(qny)
        if qant > 1:
            qnty=cart_item.quantity 
            qty=int(qnty)

            cart_item.quantity=qty - 1

            q=cart_item.quantity
            qn=int(q)

            pr=cart_item.product.product_price
            price=int(pr)

            tp=price*qn
            cart_item.total_price=tp

            cart_item.save()
            serialized_data = CartSerializer(cart_item, context={'request': request}).data
            serialized_data['image'] = str(serialized_data['image']).split('http://localhost:8000')[1]
            # for obj in serialized_data:
            #     obj['image'] = settings.MEDIA_URL + str(obj['image'])
            return Response({'data': serialized_data, 'message': 'Cart item quantity updated', 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Quantity can not be less than 1', 'success': False}, status=status.HTTP_400_BAD_REQUEST)



class Delete_CartAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = cart.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Cart successfully',  'success':True}, status=status.HTTP_200_OK)



class Get_CategoryAPIView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self, request):
        queryset = category.objects.all()
        if (queryset.count()>0):
            serializer = categorySerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'category all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class CategoryProductAPIView(GenericAPIView):
    def get(self, request, id):
        # u_id=""
        u_id = None
        qset = category.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']
            print(u_id)

        data = product.objects.filter(category=u_id).values()
        serialized_data = list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['image'] = settings.MEDIA_URL + str(obj['image'])
        return Response({'data':serialized_data, 'message':'Product category data', 'success':True}, status=status.HTTP_200_OK)



class UserReviewAPIView(GenericAPIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        user = request.data.get('user')
        feedback = request.data.get('feedback')
        product = request.data.get('product')
        rating = request.data.get('rating')
        date = request.data.get('date')
        review_status="0"


        serializer = self.serializer_class(data= {'user':user,'product':product,'feedback':feedback,'rating':rating,'date':date,'review_status':review_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Review Added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleReviewAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = brookuser.objects.all().filter(pk=id).values()
        for i in queryset:
            u_id=i['id']
        instance = Review.objects.all().filter(user=u_id).values()
        # serializer =ReviewSerializer(data)
        return Response({'data': instance, 'message':'single Review data', 'success':True}, status=status.HTTP_200_OK)


class Get_ReviewAPIView(GenericAPIView):
    serializer_class = ReviewSerializer
    def get(self, request):
        queryset = Review.objects.all()
        if (queryset.count()>0):
            serializer = ReviewSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'Review all data', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



class UserOrderAPIView(GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request):
        user = request.data.get('user')
        carts = cart.objects.filter(user=user, cart_status=0)

        if not carts.exists():
            return Response({'message': 'No items in cart to place order', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

    
        tot = carts.aggregate(total=Sum('total_price'))['total']
        total=str(tot)

        print("=========total   ",total)
        # for i in total:
        #     li.append(total)
        #     print(li)


        order_data = []
        
        for i in carts:
           

            order_data.append({
                'user': user,
                'product': i.product.id,
                'product_name': i.p_name,
                'quantity': i.quantity,
                'total_price':i.total_price,
                'image': i.image,
                'category': i.category,
                'order_status': "0",
                'all_price': total
            })
            print("order data==========",order_data)
            i.cart_status = "1"
            i.save()

        serializer = self.serializer_class(data=order_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Order placed successfully', 'success': True}, status=status.HTTP_201_CREATED)
        return Response({'data': serializer.errors, 'message': 'Failed', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


class AllPriceAPIView(GenericAPIView):
    # serializer_class = OrderPriceSerializer

    def get(self, request,id):
        # user = request.data.get('user')
        carts = cart.objects.filter(user=id, cart_status=1)
        print(carts)

        tot = carts.aggregate(total=Sum('total_price'))['total']
        Total_prices=str(tot)
        print(tot)
        
        price_status="0"

        # serializer = self.serializer_class(data= {'user':user, 'total_price':tot,'price_status':price_status})
        # print(serializer)
        # if serializer.is_valid():
        #     serializer.save()
        return Response({'data':{ 'total_price':Total_prices} , 'message': 'Get Order Price successfully', 'success': True}, status=status.HTTP_201_CREATED)
        # return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)






class SingleOrderAPIView(GenericAPIView):
    def get(self, request, id):
        qset = brookuser.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']

        # data=order.objects.all().filter(user=u_id).values()
        # print(data)

        data = order.objects.filter(user=u_id).values()
        serialized_data = list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['image'] = settings.MEDIA_URL + str(obj['image'])
        return Response({'data':data, 'message':'single order data', 'success':True}, status=status.HTTP_200_OK)





class UserOrderPaymentAPIView(GenericAPIView):
    serializer_class = PaymentSerializer

    def post(self, request):
        user = request.data.get('user')
        amount = request.data.get('amount')
        date = request.data.get('date')
        paymentstatus="1"


        serializer = self.serializer_class(data= {'user':user, 'date':date,'amount':amount,'paymentstatus':paymentstatus})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Payment successfull', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)







# class ProductAPIView(GenericAPIView):
#     serializer_class = ProductSerializer

#     def post(self, request):
#         product_name=request.data.get('product_name')
#         price = int(request.data.get('price'))
#         GST = int(request.data.get('GST'))
#         Total_price =(price * GST / 100)
#         price_total = Total_price+price
#         product_details = request.data.get('product_details')
#         stock = request.data.get('stock')
#         product_status = '0'

#         serializer = self.serializer_class(data= {'product_name':product_name,'price':price,'GST':GST,'product_price':price_total,'product_details':product_details,'stock':stock,'price_total':Total_price+price,'product_status':product_status})
#         print(serializer)
#         if serializer.is_valid():
#             print("hi")
#             serializer.save()
#             return Response({'data':serializer.data,'message':'Product added successfully', 'success':True}, status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)


# class FeedbackAPIView(GenericAPIView):
#     serializer_class = FeedbackSerializer

#     def post(self, request):
#         user=request.data.get('user')
#         product=request.data.get('product')
#         feedback = request.data.get('feedback')
#         date = request.data.get('date')
#         time = request.data.get('time')
#         feedback_status = '0'

#         serializer = self.serializer_class(data= {'user':user,'product':product,'feedback':feedback,'date':date,'time':time,'feedback_status':feedback_status})
#         print(serializer)
#         if serializer.is_valid():
#             print("hi")
#             serializer.save()
#             return Response({'data':serializer.data,'message':'feedback added successfully', 'success':True}, status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)




# class CartAPIView(GenericAPIView):
#     serializer_class = CartSerializer

#     def post(self, request):
#         user=request.data.get('user')
#         product=request.data.get('product')
#         price = request.data.get('price')
#         # Image = request.data.get('Image')
#         Quantity = request.data.get('Quantity')
#         cart_status = '0'

#         serializer = self.serializer_class(data= {'user':user,'product':product,'price':price,'Quantity':Quantity,'cart_status':cart_status})
#         print(serializer)
#         if serializer.is_valid():
#             print("hi")
#             serializer.save()
#             return Response({'data':serializer.data,'message':'cart added successfully', 'success':True}, status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)


# class OrderAPIView(GenericAPIView):
#     serializer_class = OrderSerializer

#     def post(self, request):
    
#         product=request.data.get('product')
#         price = request.data.get('price')
#         # Image = request.data.get('Image')
#         date = request.data.get('date')
#         time = request.data.get('time')
#         Quantity = request.data.get('Quantity')
#         order_status = '0'

#         serializer = self.serializer_class(data= {'product':product,'price':price,'date':date,'time':time,'Quantity':Quantity,'order_status':order_status})
#         print(serializer)
#         if serializer.is_valid():
#             print("hi")
#             serializer.save()
#             return Response({'data':serializer.data,'message':'order successfully', 'success':True}, status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)













           