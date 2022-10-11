import sys

import random


def define_coOrdinator():

    '''

    Here we define the present coordinator among the processes

    '''

    coordinator = int(input('Enter the coordinator process id: '))

    while True:

        if coordinator in process:

            return coordinator

        else:

            print("Process id is not available in the process list")

            coordinator = int(input('Enter the coordinator process id: '))




def ring(initiator):

    '''  

    This function defines the ring structure of the process

    '''

    ids_ring = []

    ids_ring.append(initiator)

    # if ring is in low to high only

    # ids_ring = sorted(process)

   

    # if ring is in random order

    n=0


    while n!=(len(process)-1):

        temp = random.randrange(0, len(process))

        if process[temp] not in ids_ring:

            ids_ring.append(process[temp])

            n += 1

   

    return ids_ring


def elect_coordinator(initiator, ring_order):

   

    '''

    Elects the new coordinator

    '''


    print(f'''

        <------------------- Ring order ------------------>

                {ring_order}

    ''')

    new_coordinator = max(process)

    for i in ring_order:

        ''' we will be assuming error if we get 7 as a random number. In that case we will conduct re-election'''

        if random.randrange(0, 10) == 7:

            print("error in declaraing new co-ordinator")

            print("<-----------------------Re-election----------------------> ")

            elect_coordinator(initiator,ring_order)

        else:

            print(f'messaged suceesfully send from process{i}')

   

    print(f'''

            ****************Election Successfull*****************

            new co-ordinator is process {new_coordinator}

    ''')



def remove_coordinator(request_id, coordinator):

    process.remove(coordinator)

    print(f'''

        coordinator {coordinator} is dead.

        process {request_id} finds out and initiates the election process for new co-ordinator.

    ''')

    elect_coordinator(request_id, ring(request_id))    



def check_coordinatorStatus(request, coordinator):

    '''

        flag 1 for OK coordinator status

        flag 0 for DEAD coordinator status

     '''

    print(f'''  

            CHOOSE:

            1   :   for OKAY Status

            0   :   for DEAD Status

    ''')

    # co = coordinator()

    while True:

        flag = int(input('Choose one: '))

        if flag == 1 :

            print(f'process id {request} sucessefully requested the coordinator {coordinator}')

        elif flag == 0:

            # print(f'coordinator{coordinator} is dead.')

            remove_coordinator(coordinator=coordinator, request_id = request)

            return


if __name__=='__main__':

    process = []
    #initiating with 5 process
    no_of_processes =5

    for i in range(no_of_processes):

        temp = int(input("Enter process id: "))

        if temp not in process:

            process.append(temp)

            print("process ids are :", process)

        else:

            print("Prcess id already exists.. ")

            temp = int(input("Enter process id: "))

            process.append(temp)


    '''

    Let us consider Process no 2 i.e process[1] is requesting coordinator for performing actions.

    ''' 

    check_coordinatorStatus(process[1], define_coOrdinator())

    # remove_coordinator()

