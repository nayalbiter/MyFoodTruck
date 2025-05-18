from flask import redirect, render_template, request, url_for
from utils.getFoodTruckInfo import getFoodTruckDetails


def editFoodTruckDetails():
    
    food_truck_id = request.form.get('food_truck_id')
    print(f"this is the food truck id : {food_truck_id}")
    
    if not food_truck_id:
        print("something is wrong with the food truck id, no found")
        return redirect(url_for("go2CompanyMainPageAfterLogIn"))
    
    truckInfo = getFoodTruckDetails(food_truck_id)
    
    if not truckInfo:
        print("this food truck does not exist")
        return redirect(url_for("go2CompanyMainPageAfterLogIn"))
    
    return render_template("editFoodTruckDetails.html", truck = truckInfo)
    