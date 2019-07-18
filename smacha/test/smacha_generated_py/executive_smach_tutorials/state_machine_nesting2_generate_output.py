#!/usr/bin/env python




import roslib; roslib.load_manifest('smacha')
import rospy
import smach
import smach_ros








# define state Bas
class Bas(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAS')
        return 'outcome3'

# define state Foo
class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        if self.counter < 3:
            self.counter += 1
            return 'outcome1'
        else:
            return 'outcome2'

# define state Bar
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR') 
        return 'outcome1'









def main():
    rospy.init_node('smach_example_state_machine')

    



    sm_top = smach.StateMachine(outcomes=['outcome5'])




    with sm_top:

        smach.StateMachine.add('BAS', Bas(),
                               transitions={'outcome3':'SUB'})

        sm_sub = smach.StateMachine(outcomes=['outcome4'])




        with sm_sub:

            smach.StateMachine.add('FOO', Foo(), 
                                   transitions={'outcome1':'BAR',
                                                'outcome2':'outcome4'})

            smach.StateMachine.add('BAR', Bar(), 
                                   transitions={'outcome1':'FOO'})



        smach.StateMachine.add('SUB', sm_sub,
                               transitions={'outcome4':'outcome5'})



        





    

    outcome = sm_top.execute()





    



if __name__ == '__main__':
    main()