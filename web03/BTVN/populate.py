from models.service import Service
import mlab
from faker import Faker
from random import randint, choice, sample

mlab.connect()

fake = Faker()

male_link = [
    "https://mediaslide-europe.storage.googleapis.com/premier/pictures/4210/13997/profile-1523974858-839fb415d8b9d884a822c781536d4aa6.jpg",
    "https://sguru.org/wp-content/uploads/2017/04/facebook-profile-photo-boy-stylish-32.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn0Z00vvAW5Iyz0qJIc2FFsfCL7E4C94sJwI0e24sBCP0c-8IR",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHVotRDooYTnrdPLVhf2dFIvxqmW1-_-LVzvHQ0hMoUkgTu-c-",
    "https://assets.capitalfm.com/2013/01/zayn-malik-1357748046-view-0.jpg"
]

female_link =[
    "https://images.pexels.com/photos/733872/pexels-photo-733872.jpeg?cs=srgb&dl=fashion-person-woman-733872.jpg&fm=jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2qGWfezwFJYq97QsrbUb_aGV3zzoqe9algLjst_OxvURCZjLN",
    "http://bdfjade.com/data/out/84/5896245-girl-profile-picture.jpg",
    "https://www.edatingdoc.com/wp-content/thesis/skins/edatingdoc/images/Female-Opinion-Dating-24116.jpg",
    "https://i0.wp.com/tricksmaze.com/wp-content/uploads/2017/04/Stylish-Girls-Profile-Pictures-32.jpg?resize=500%2C500&ssl=1"
]


for i in range(50):
    print("saving service",i+1,".......")

    sex = randint(0,1)
    if sex ==1:
        link =choice(male_link)
        des = sample(["ga lăng","giàu","đẹp trai","to","cao","lãng tử","đen"],3)
    else:
        link = choice(female_link)
        des = sample(["ngoan hiền","lễ phép với gia đình","thông minh","dễ thương","kute","xinh","ngon"],3)

    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000),
        gender = sex,
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        Status = choice([True,False]),
        image = link,
        description = ','.join(des),
        measurements = [randint(80,100),randint(60,90),randint(80,100)]
    )

    new_service.save()

