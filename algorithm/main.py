import collections

'''

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
//求和0的数量

'''

class Solusion:

    def countPalindromicSubsequences(self, S: str) -> int:
        N = len(S)
        MOD = 1000000007
        nxt = [0] * N
        use = [0] * N
        ans = 0
        for j in range(N):
            x = 1
            for i in range(j - 1, -1, -1):
                if S[i] == S[j]:
                    now_nxt = nxt[i]
                    now_use = use[i]
                    nxt[i] += x
                    x = now_nxt - now_use + 1
                    use[i] = now_nxt + 1
                else:
                    nxt[i] += x
            ans += x
        return ans % MOD


if __name__ == '__main__':
    print(Solusion().countPalindromicSubsequences("abcdba"))