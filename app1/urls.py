from django.urls import path
from app1 import views

urlpatterns = [
   path('',views.user_home),
   path('home/',views.login_home),
   path('about/',views.about),
   path('blog/',views.blog),
   path('blog-details/',views.blog_details),
   path('contact/',views.contact),
   path('user_registrations/',views.user_registrations),
   path('user_view_update_profile/',views.user_view_update_profile),
   path('user_login/',views.user_login),
   path('user_profile/',views.user_profile),
   path('cats/',views.adopt_cats),
   path('dogs/',views.adopt_dogs),
   path('birds/',views.adopt_birds),
   path('fishes/',views.adopt_fishes),
   path('cat_food/',views.cat_food),
   path('dog_food/',views.dog_food),
   path('bird_food/',views.bird_food),
   path('fish_food/',views.fish_food),
   path('shop_list/',views.shop_list),
   path('pets_details/',views.pets_details),
   path('food_details/',views.food_details),  
   path('clear_mycart/',views.clear_mycart),
   path('delete_cartitem/',views.delete_cartitem),
   path('pets_addcart/',views.pets_addcart),
   path('food_addcart/',views.food_addcart),
   path('buynow/',views.buynow),
    path('cart/',views.cart),
   path('makepayment/',views.makepayment),
   path('cancelpayment/',views.cancelpayment),
   path('mypayments/',views.mypayments),
   path('orders/',views.orders),
   path('checkout/',views.checkout),
   path('wishlist/',views.wishlist),
   path('login-register/',views.login_register),
   path('shop/',views.shop),

   path('review/',views.review),
   path('view_veterinerians/',views.view_veterinerians),
   path('tutorials/',views.tutorials),

  
####################################---ADMIN---##################################################
   path('login/',views.admin_login),
   path('admin_home/',views.admin_home),
   path('add_pets/',views.add_pet),
   path('admin_approve_shop/',views.admin_approve_shop),
   path('admin_reject_shop/',views.admin_reject_shop),
   path('admin_reject_pets/',views.admin_reject_pets),
   path('admin_reject_user/',views.admin_reject_user),
   path('view_user/',views.view_user),
   path('view_shop/',views.view_shop),
   path('view_pets/',views.view_pets),
   path('view_orders/',views.view_orders),
   path('admin_view_reject_shop/',views.admin_view_reject_shop),
   path('admin_view_approved_shop/',views.admin_view_approved_shop),
   path('admin_view_reject_pets/',views.admin_view_reject_pets),
   path('admin_view_reject_user/',views.admin_view_reject_user),
   path('admin_update_pet/',views.admin_update_pet),
   path('admin_view_update_pet/',views.admin_view_update_pet),
   path('admin_view_user_payment/',views.admin_view_user_payment),
   # path('admin_view_shop_rejected_user/',views.admin_view_shop_rejected_user),
   path('admin_change_password/',views.admin_change_password),
   
   path('paytoshop/',views.paytoshop),
   path('admin_makepayment/',views.admin_makepayment),
   path('admin_cancelpayment/',views.admin_cancelpayment),

   path('view_foods/',views.view_foods),
      #orders to admin
   path('admin_view_orders/',views.admin_view_orders),
   path('admin_view_processing/',views.admin_view_processing),
   path('admin_view_shipped/',views.admin_view_shipped),
   path('admin_view_completed/',views.admin_view_completed),
   path('admin_processing/',views.admin_processing),
   path('admin_shipping/',views.admin_shipping),
   path('admin_delivered/',views.admin_delivered),

   path('view_vetenery/',views.view_vetenery),
   path('admin_view_approved_vetenery/',views.admin_view_approved_vetenery),
   path('admin_view_reject_vetenery/',views.admin_view_reject_vetenery),






  ###############################---PET-SHOP---######################################################


   path('shop_login_register/',views.shop_login_register),
   path('shop_registrations/',views.shop_registrations),
   path('shop_login/',views.shop_login),
   path('shop_home/',views.shop_home),
   path('shop_profile/',views.shop_profile),
   path('shop_add_pets/',views.shop_add_pets),
   path('shop_add_food/',views.shop_add_food),
   path('shop_reject_pets/',views.shop_reject_pets),
   path('shop_reject_food/',views.shop_reject_food),
   path('shop_view_user/',views.shop_view_user),
   # path('shop_view_shop/',views.shop_view_shop),
   path('shop_view_pets/',views.shop_view_pets),
   path('shop_view_food/',views.shop_view_food),
   path('shop_view_orders/',views.shop_view_orders),
   # path('shop_view_approved_shop/',views.shop_view_approved_shop),
   # path('shop_view_rejected_shop/',views.shop_view_rejected_shop),
   path('shop_view_rejected_pets/',views.shop_view_rejected_pets),
   path('shop_view_rejected_food/',views.shop_view_rejected_food),
   # path('shop_approve_user/',views.shop_approve_user),
   # path('shop_reject_user/',views.shop_reject_user),
   path('shop_view_rejected_user/',views.shop_view_rejected_user),
   path('shop_userorder_completed/',views.shop_userorder_completed),
   path('shop_view_applied_user/',views.shop_view_applied_user),
   path('shop_view_previous_order/',views.shop_view_previous_order),
   path('shop_view_user_payment/',views.shop_view_user_payment),
   path('shop_update_pet/',views.shop_update_pet),
   path('shop_view_update_pet/',views.shop_view_update_pet),
   path('shop_update_food/',views.shop_update_food),
   path('shop_view_update_food/',views.shop_view_update_food),
   path('logout/',views.logout),
   path('shop_view_processing/',views.shop_view_processing),
   path('shop_view_shipped/',views.shop_view_shipped),
   path('shop_view_completed/',views.shop_view_completed),
   path('shop_processing/',views.shop_processing),
   path('shop_shipping/',views.shop_shipping),
   path('shop_delivered/',views.shop_delivered),
   path('shop_mypayments/',views.shop_mypayments),



######################################################
 path('vetenery_login/',views.vetenery_login),
 path('vetenery_login_register/',views.vetenery_login_register),
 path('vetenery_registrations/',views.vetenery_registrations),
 path('personal_vetenery/',views.personal_vetenery),
 path('qualexp_vetenery/',views.qualexp_vetenery),
 path('consult_vetenery/',views.consult_vetenery),
 path('chngepwd_vetenery/',views.chngepwd_vetenery),






]
