class Character(object):
    def __init__(self, name, hp, damage, attack_speed, armor):
        self.name = name
        self.damage = damage
        self.health = hp
        self.attack_speed = attack_speed
        self.bag = []
        self.armor = armor
        
    def pick_up(self, item):
        self.bag.append(item)
        print "You put the %s in your bag." % item
        
    def attack(self, target):
        target.take_damage(self.damage)
        print "You attacked %s for %d damage." % (target.name , self.damage)
        
    def take_damage(self, damage):
        if self.armor > 0:
            self.armor -= damage
            if self.armor <= 0:
                if self.health > 0:
                    self.health -= damage
        else:
            print "%s is already dead" % self.name
        
orc1 = Character('The First Orc', 100, 20, 2, 0)
orc2 = Character('The Second Orc', 100, 20, 2, 0)
sam = Character("Sam V", 10, 0.000000000001, 0.0000000001, 50)
ed = Character('Edwin Burgos', 9001, 2, 1, 500)
rob = Character('Roberto Moreno', 80, 100, 2, 200)
bob = Character('Bobby Vixathep', 1, 20, 2, 0)
wiebe = Character('Senor Wiebe', 300, 66, 2, 200)