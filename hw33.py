class Godzilla:
    FULNESS = 90

    def __init__(self, name, volume_of_stomach, max_amount_of_people_in_portion):
        self.name = name
        self.volume_of_stomach = volume_of_stomach
        self.max_amount_of_people_in_portion = max_amount_of_people_in_portion
        self.people_in_stomach_now = 0


    def print_info(self):
        print('----0-----0----')
        print('------|-|------')
        print('-----\|||/----')
        print('\nHi, i am godzilla, my name is %s.' % self.name)
        print('I can digest maximum %d people at once...' % self.volume_of_stomach)
        print('I can eat maximum %d people at once...' % self.max_amount_of_people_in_portion)
        print('There are %d people in my stomach now.' %  self.people_in_stomach_now)

    def eat_people(self):
        import random
        while self.people_in_stomach_now <= self.volume_of_stomach * Godzilla.FULNESS / 100:
            print('\n\nHmm, wanna feed me ? yw...')
            print('There are %d people in my stomach now.' % self.people_in_stomach_now)
            print(input('\nPress Enter to feed me ...'))
            people = random.randint(1, self.max_amount_of_people_in_portion)
            self.people_in_stomach_now += people
            print('%d people accepted' % people)
        if self.people_in_stomach_now > self.volume_of_stomach:
            print('...that portion too big...\n...stomach have bursted...%s have died' % self.name)
        else:
            print('\nYeeeeeaaaah, I\'m full!')


godzilla1 = Godzilla('Kesha', 30, 7)
godzilla1.print_info()
godzilla1.eat_people()
