  # CMPS 6610 Problem Set 01
## Answers

**Name:** Md. Ahsan Habib


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 

    - ***Answer***

      $O(f(n)) = \{g(n) \mid f(n) \text{ asymptotically dominates } g(n)\}$

      To determine if $2^n$ asymptotically dominates $2^{n+1}$, we need to find constants $c > 0$ and $n_0$ such that:

      $$
      2^{n+1} \leq c \cdot 2^n \quad \text{for all } n \ge n_0
      $$

      Dividing both sides by $2^n$, we get:

      $$
      2 \leq c
      $$

      So, any $c \geq 2$ and any $n_0 \geq 0$ will work. For example, if we set $c = 2$ and $n_0 = 0$, the inequality holds for all $n \geq 0$:

      $$
      2^{n+1} \leq 2 \cdot 2^n
      $$

      Thus, $2^{n+1} \in O(2^n)$.

    <!-- 1a answer ends here -->



  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?  

    - ***Answer***  

      $O(f(n)) = \{g(n) \mid f(n) \text{ asymptotically dominates } g(n)\}$

      To determine if $2^{2^n} \in O(2^n)$, we need to check if there exist constants $c > 0$ and $n_0$ such that:

      $$
      2^{2^n} \leq c \cdot 2^n \quad \text{for all } n \geq n_0
      $$

      However, $2^{2^n}$ grows much faster than $2^n$. In fact, for large $n$, $2^{2^n} \gg 2^n$.

      Taking logarithms of both sides:

      $$
      \log_2(2^{2^n}) = 2^n \quad \text{and} \quad \log_2(c \cdot 2^n) = \log_2 c + n
      $$

      For large $n$, $2^n$ grows much faster than $n$, so the inequality cannot be satisfied for any constant $c$.

      Therefore, $2^{2^n} \notin O(2^n)$.

    <!-- 1b answer ends here -->
  


  - 1c. Is $n^{1.01} \in O(\mathrm{\log}^2 n)$?

    - ***Answer***

      $O(f(n)) = \{g(n) \mid f(n) \text{ asymptotically dominates } g(n)\}$

      To determine if $n^{1.01} \in O((\log n)^2)$, we need to check if there exist constants $c > 0$ and $n_0$ such that:

      $$
      n^{1.01} \leq c \cdot (\log n)^2 \quad \text{for all } n \geq n_0
      $$

      However, for large $n$, any positive power of $n$ grows much faster than any power of $\log n$. In particular, $n^{1.01} \gg (\log n)^2$ as $n \to \infty$.

      Taking logarithms of both sides:

      $$
      \log(n^{1.01}) = 1.01 \log n \quad \text{and} \quad \log(c (\log n)^2) = \log c + 2 \log \log n
      $$

      For large $n$, $1.01 \log n$ grows much faster than $2 \log \log n$, so the inequality cannot be satisfied for any constant $c$.

      Therefore, $n^{1.01} \notin O((\log n)^2)$.


  <!-- 1c answer ends here -->


  - 1d. Is $n^{1.01} \in \Omega(\mathrm{\log}^2 n)$?

    - ***Answer***

      $\Omega(f(n)) = \{g(n) \mid g(n) \text{ asymptotically dominates } f(n)\}$

      To determine if $n^{1.01} \in \Omega((\log n)^2)$, we need to check if there exist constants $c > 0$ and $n_0$ such that:

      $$
      n^{1.01} \geq c \cdot (\log n)^2 \quad \text{for all } n \geq n_0
      $$

      For large $n$, any positive power of $n$ grows much faster than any power of $\log n$. In particular, $n^{1.01} \gg (\log n)^2$ as $n \to \infty$.

      Taking logarithms of both sides:

      $$
      \log(n^{1.01}) = 1.01 \log n \quad \text{and} \quad \log(c (\log n)^2) = \log c + 2 \log \log n
      $$

      For large $n$, $1.01 \log n$ grows much faster than $2 \log \log n$, so the inequality is satisfied for sufficiently large $n$ and some $c > 0$.

      Therefore, $n^{1.01} \in \Omega((\log n)^2)$.



  - 1e. Is $\sqrt{n} \in O(\mathrm{\log}^3 n)$? 

    - ***Answer***

      $O(f(n)) = \{g(n) \mid f(n) \text{ asymptotically dominates } g(n)\}$

      To determine if $\sqrt{n} \in O((\log n)^3)$, we need to check if there exist constants $c > 0$ and $n_0$ such that:

      $$
      \sqrt{n} \leq c \cdot (\log n)^3 \quad \text{for all } n \geq n_0
      $$

      For large $n$, any positive power of $n$ grows much faster than any power of $\log n$. In particular, $\sqrt{n} = n^{1/2} \gg (\log n)^3$ as $n \to \infty$.

      Taking logarithms of both sides:

      $$
      \log(\sqrt{n}) = \frac{1}{2} \log n \quad \text{and} \quad \log(c (\log n)^3) = \log c + 3 \log \log n
      $$

      For large $n$, $\frac{1}{2} \log n$ grows much faster than $3 \log \log n$, so the inequality cannot be satisfied for any constant $c$.

      Therefore, $\sqrt{n} \notin O((\log n)^3)$.




  - 1f. Is $\sqrt{n} \in \Omega(\mathrm{\log}^3 n)$?

    - ***Answer***

      $\Omega(f(n)) = \{g(n) \mid \exists\ c > 0,\ n_0 \text{ such that } g(n) \geq c \cdot f(n) \text{ for all } n \geq n_0\}$

      To determine if $\sqrt{n} \in \Omega((\log n)^3)$, we need to check if there exist constants $c > 0$ and $n_0$ such that:

      $$
      \sqrt{n} \geq c \cdot (\log n)^3 \quad \text{for all } n \geq n_0
      $$

      For large $n$, any positive power of $n$ grows much faster than any power of $\log n$. In particular, $\sqrt{n} = n^{1/2} \gg (\log n)^3$ as $n \to \infty$.

      Taking logarithms of both sides:

      $$
      \log(\sqrt{n}) = \frac{1}{2} \log n \quad \text{and} \quad \log(c (\log n)^3) = \log c + 3 \log \log n
      $$

      For large $n$, $\frac{1}{2} \log n$ grows much faster than $3 \log \log n$, so the inequality is satisfied for sufficiently large $n$ and some $c > 0$.

      Therefore, $\sqrt{n} \in \Omega((\log n)^3)$.
      


  - 1g. Consider the definition of "Little o" notation:
  
$g(n) \in o(f(n))$ means that for **every** positive constant $c$, there exists a constant $n_0$ such that $g(n) \le c \cdot f(n)$ for all $n \ge n_0$. There is an analogous definition for "little omega" $\omega(f(n))$. The distinction between $o(f(n))$ and $O(f(n))$ is that the former requires the condition to be met for **every** $c$, not just for some $c$. For example, $10x \in o(x^2)$, but $10x^2 \notin o(x^2)$.  

.  

**Prove** that $o(g(n)) \cap \omega(g(n))$ is the empty set.

  - ***Proof***
    - $f(n) \in o(g(n))$ means that for **every** $c > 0$, there exists $n_0$ such that $f(n) \leq c \cdot g(n)$ for all $n \geq n_0$.
    - $f(n) \in \omega(g(n))$ means that for **every** $c > 0$, there exists $n_0$ such that $f(n) \geq c \cdot g(n)$ for all $n \geq n_0$.

    Suppose, for contradiction, that there exists a function $f(n)$ such that $f(n) \in o(g(n)) \cap \omega(g(n))$.

    Then, by definition:
    - For every $c > 0$, $f(n) \leq c \cdot g(n)$ for all sufficiently large $n$.
    - For every $c > 0$, $f(n) \geq c \cdot g(n)$ for all sufficiently large $n$.

    Take $c = 1$. Then for large $n$,
    $$
    f(n) \leq g(n) \quad \text{and} \quad f(n) \geq g(n)
    $$
    So $f(n) = g(n)$ for all sufficiently large $n$.

    Now take $c = 1/2$. Then for large $n$,
    $$
    f(n) \leq \frac{1}{2}g(n) \quad \text{and} \quad f(n) \geq \frac{1}{2}g(n)
    $$
    So $f(n) = \frac{1}{2}g(n)$ for all sufficiently large $n$.

    But this is only possible if $g(n) = 0$ for large $n$, which is not generally the case for nontrivial $g(n)$.

    Therefore, no function can be in both $o(g(n))$ and $\omega(g(n))$ unless $g(n)$ is eventually zero, so:
    $$
    o(g(n)) \cap \omega(g(n)) = \emptyset
    $$

2. **SPARC to Python**

  - 2b

3. **Parallelism and recursion**

  - 3b

  - 3d

  - 3e
  
4. **GCD**
  
