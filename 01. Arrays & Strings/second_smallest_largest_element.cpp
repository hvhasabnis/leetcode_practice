// Question : Find Second Smallest and Second Largest Element in an array
#include <iostream>
#include <vector>
#include <utility> //required for pair
using namespace std;

class Solution
{
public:
    pair<int, int> secondLargestElement(vector<int> &nums)
    {
        for (size_t i = 0; i < nums.size() - 1; i++)
        {
            bool swapped = false;
            for (size_t j = 0; j < nums.size() - i - 1; j++)
            {
                if (nums[j] > nums[j + 1])
                {
                    swapped = true;
                    swap(nums[j], nums[j + 1]);
                }
            }

            if (!swapped)
            {
                break;
            }
        }

        int secondLargest = nums[nums.size() - 1];
        int secondSmallest = nums[0];

        for (size_t i = 1; i < nums.size(); i++)
        {
            if (secondSmallest > nums[i])
            {
                
            }

            if (secondSmallest > nums[i])
            {

            }
        }
    }
};

int main(int argc, char const *argv[])
{
    Solution solution = Solution();

    pair<int, int> result = solution.secondLargestElement({8, 8, 7, 6, 5});

    cout << "Second Largest element is " << result.first << endl;

    cout << "Second Smallest element is " << result.second << endl;

    return 0;
}
