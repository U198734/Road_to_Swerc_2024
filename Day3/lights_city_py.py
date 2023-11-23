# Swerc 2018
import sys
 
def max_lights(N, K, attack_positions):
    lights = [1] * (N + 1)
    maxx = 0
    current = 0
 
    for s in range(K):
        i = attack_positions[s]
        i_ = i
        while (i_ <= N):
            if lights[i_] == 0:
                lights[i_] = 1
                current -= 1
            else:
                lights[i_] = 0
                current += 1
            i_ += i
        if current > maxx:
            maxx = current
 
    return maxx
 
if __name__ == "__main__":
    N = int(sys.stdin.readline().strip()) # num de llums
    K = int(sys.stdin.readline().strip()) # num de attacks
    attack_positions = [int(sys.stdin.readline().strip()) for _ in range(K)]
 
    result = max_lights(N, K, attack_positions)
    print(result)