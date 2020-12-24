def solution(participant, completion):
    answer = ''
    answer = participant - completion
    #for i in range(0,len(participant)):
        #for j in range(0,len(completion)):
            #if participant[i] != completion[j]:
                #answer = participant[i]
    return answer

participant1 = ["leo", "kiki", "eden"]
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
participant3 = ["mislav", "stanko", "mislav", "ana"]

completion1 = ["eden", "kiki"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
completion3 = ["stanko", "ana", "mislav"]

print("return1 = ",solution(participant1,completion1))
print("return2 = ",solution(participant2,completion2))
print("return3 = ",solution(participant3,completion3))