class Character(object):
    def __init__(self, name, hp, damage, attack_speed):
        self.name = name
        self.damage = damage
        self.health = hp
        self.attack_speed = attack_speed
        self.bag = []
        
    def pick_up(self, item):
        self.bag.append(item)
        print "You put the %s in your bag." % item
        
    def attack(self, target):
        target.take_damage(self.damage)
        print "You attacked %s for %d damage." % (target.name , self.damage)
        
    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            if self.health <= 0:
                print "%s has been slain," %self.name
        else:
            print "%s is already dead" % self.name
        
orc1 = Character('The First Orc', 100, 20, 2)
orc2 = Character('The Second Orc', 100, 20, 2)
sam = Character("Sam V", 10, 0.000000000001, 0.0000000001)

#Testing code
orc1.attack(orc2)
print "The second orc has %d health." % orc2.health