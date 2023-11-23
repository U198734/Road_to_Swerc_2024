#include <iostream>
#include <vector>
 
int main() {
    int N, K;
    std::cin >> N; // num de llums
    std::cin >> K; // num de attacks
    
    std::vector<int> attack_positions(K);
    for (int i = 0; i < K; ++i) {
        std::cin >> attack_positions[i];
    }
 
    std::vector<int> lights(N + 1, 1);
    int maxx = 0;
    int current = 0;
 
    for (int s = 0; s < K; ++s) {
        int i = attack_positions[s];
        int i_ = i;
        while (i_ <= N) {
            if (lights[i_] == 0) {
                lights[i_] = 1;
                current -= 1;
            } else {
                lights[i_] = 0;
                current += 1;
            }
            i_ += i;
        }
        if (current > maxx) {
            maxx = current;
        }
    }
 
    std::cout << maxx << std::endl;
 
    return 0;
}