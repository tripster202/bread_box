// example file of how pointers work

// include <iostream>
// include <string>
using namespace std;

int main() {

// pass value by reference

   string food = "Pizza";
   string &dinner = food;

   cout << food << "\n";
   cout << dinner << "\n";

   // pointers

   string food = "Pizza";

   cout << food << "\n";
   cout << &food << "\n";

   return 0;
}

// https://www.w3schools.com/cpp/cpp_references.asp
// https://www.w3schools.com/cpp/cpp_pointers.asp