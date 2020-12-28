from django.shortcuts import render

print("Getting started!!","\n")
shibas = [
    {
        'image_src': 'https://i.imgur.com/VEslUBl.png',
        'name': 'Tacopup',
        'age': 2,
        'id_number': 1,
    },
    {
        'image_src': 'https://i.imgur.com/iCCNZZF.jpg',
        'name': 'Pupperwave',
        'age': 3,
        'id_number': 2,
    },
    {
        'image_src': 'https://i.imgur.com/XiznnoN.jpg',
        'name': 'Wow-Banana',
        'age': 5,
        'id_number': 3,
    },
    {
        'image_src': 'https://i.imgur.com/ORizDRq.png',
        'name': 'Galaxy-Doggo',
        'age': 2,
        'id_number': 4,
    },
    {
        'image_src': 'https://i.imgur.com/APMdtxs.png',
        'name': 'Sweetdoggo',
        'age': 4,
        'id_number': 5,
    },
]

def homepage(request):
    print("homepage getting viewed")
    count = len(shibas)
    context = {
        'shiba_count': count,
        'all_shibas': shibas,
    }
    return render(request, 'homepage.html', context)



def adoption(request):
    print("adoption page getting viewed")

    if 'number' in request.GET:
        number = int(request.GET['number'])
        print('They entered:', number)
        for shiba in shibas:
          if shiba['id_number'] == number:
            print('found shiba, removing!')
            shibas.remove(shiba)

    context = {
    }
    return render(request, 'adoption_page.html', context)


def shiba_add(request):
    print("add shiba page getting viewed")

    if 'dog_name' in request.GET:
        the_name = request.GET['dog_name']
        the_age = request.GET['dog_age']
        print('name received:', the_name)
        print('age received:', the_age)
        count = len(shibas)
        name_dict = {
            'image_src': 'https://i.imgur.com/APMdtxs.png',
            'name': the_name,
            'age': the_age,
            'id_number': count + 1,
    }
        shibas.append( name_dict )

    context = {
    }
    return render(request, 'add_shiba.html', context)