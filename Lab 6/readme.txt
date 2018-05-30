Christina Oliveira
TA:Dhavalikar
Section 5
UID: 204803448
Lab 6: Multithreaded Performance

I ran into many issues implementing this switch to
multithreading. Though I understand threading well (from cs33)
it took me a while to understand what the current main was doing and 
how I could implement threading. I realized that why wad confusing me 
is that there was no auxiliary function present that could be used to 
send the threads to, and that in this case, I needed to make one. I also 
realized that the for loops already present only 
needed to be augmented with thread join and
create, and that the auxiliary function could do most of the rest.
I also ran into several problems when making the file.
At first, I wasn't able to make it at all, as it said it did not
recognize the functions pthreadjoin and create, this turned out to be
because I did not link the library in the Makefile. Frustratingly, this 
was the error that took me the longest to figure out!
I also had a joining issue, where a thread was left hanging.
Once everything was working I was able to successfully run the command
make clean check
which had the output shown in the make-log.txt file, The results of the
time tests (copy pasted from said file) are as such:

test1
real	0m42.907s
user	0m42.899s
sys	0m0.002s

test2
real	0m22.109s
user	0m43.957s
sys	0m0.001s

test4
real	0m11.112s
user	0m44.202s
sys	0m0.002s

test 8
real	0m5.702s
user	0m44.342s
sys	0m0.002s

This shows that as the number of threads increases, the time required for execution
goes down drastically from over 40 to 5, this is aprox. an 8x speedup, as expected,
as for every task in the single threaded can do in a second, the 8-threaded 
can do 8 tasks. This makes the speedup aprox. linear.



