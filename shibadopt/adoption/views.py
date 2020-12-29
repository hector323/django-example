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

    context = {}  # No need for context on this page

    if 'name' in request.GET:
        age = int(request.GET['age'])
        name = request.GET['name']
        print('They entered:', name)

        id_number = len(shibas)

        # Add a new shiba, make it a taco shiba
        shibas.append({
            'age': age,
            'name': name,
            'id_number': id_number,
            'image_src': 'https://i.imgur.com/VEslUBl.png',
        })

    return render(request, 'add_shiba.html', context)