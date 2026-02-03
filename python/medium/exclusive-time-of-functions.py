from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # duration = End Timestamp - Start Timestamp + 1

        result = [0 for x in range(n)]
        stack = []

        # we will have to make a for loop and look at the timestamps one by one.
        # looking at the first one, we will have to push 0 onto the stack

        # now we can see 1, since its a start operation
        # we update the time of last element on the stack
        # result[stack.peek()] = current_time - prev_time

        prev_time = 0
        
        for log in logs:
            print(log)
            strings = log.split(":")
            log_id = int(strings[0])
            log_status = strings[1]
            log_time = int(strings[2])

            # How do we check if the log_id has ever been added? do we need to check for that



            # we add the first log_id to the stack, no need to update any values
            if len(stack) == 0:
                prev_time = log_time
                stack.append(log_id)
                continue

            # in this case the stack is not empty, we can 
            if log_id not in stack:
                result[stack[-1]] += log_time - prev_time
                prev_time = log_time
                stack.append(log_id)
                continue
            
            if log_status == "start":
                result[stack[-1]] += log_time - prev_time
                prev_time = log_time
            
            elif log_status == "end":
                result[stack.pop()] += log_time - prev_time + 1
                prev_time = log_time + 1
                
        print(result)
        return result 


if __name__ == "__main__":
    Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])