---
title: 'Proof of the Triple Product Rule'
pubDate: 'Aug 10 2025'
revDate: 'Apr 3 2026'
description: "Satisfying (to me) proofs of the Triple Product Rule and an unnamed 4-variable identity: two identities of 2D surfaces in 3D space"
author: conjuncts
heroImage: '../../assets/3-partial.svg'
tags: ["math"]
---

## P3. Unstated Assumptions

Unlike mathematicians, who are typically very scrupulous about exact conditions under which theorems and equations hold, introductory thermodynamics omits a shocking amount of information.

Partial derivatives -- for example $\pdc{P}{T}{V}$ - are often presented without any mention of whether P can be even written in terms of T and V at all, whether these functions exist or if 2 variables is enough, too many, or too few variables to describe the underlying surface. 

What is the domain of these functions? Does P accept 2, 3, or more variables? Are we working with $\mathbb{R}^2 \to \mathbb{R}$, or something different? How do we know that everything is differentiable as claimed?



## S1. Stated Assumptions

First, a **gigantic** assumption, unfortunately often unmentioned, is the [state postulate](https://en.wikipedia.org/wiki/State_postulate). This states that 2 independent variables are often enough to define a thermodynamic state. 

This means we often work with a 2D manifold in thermodynamic space (for instance, the PvT surface is indeed a surface.) Without this assumption, many problems seem ill-posed in the sense of having many or no solutions. More generally, the Gibbs phase rule can be used to to get the dimension.

Also note that in thermodynamics, it can often be assumed that **variables are interdependent**. So if we have P, V, T, assume that each can be written in terms of the other 2 - that all those functions exist.

(Actually, sometimes variables are not globally interdependent. But thanks to what's known as the [Implicit Function Theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem), what we can say is that locally, near a point, the variables are often interdependent)


## Additional gripes and future directions

My biggest gripe is that thermodynamics makes some huge assumptions that often go untaught. Here are the major ones:

- Not mentioning the state postulate.
    - PLEASE mention the state postulate.
    - Without this assumption, if you don't know it's a 2D manifold, many problems seem ill-posed in the sense of having many or no solutions.
- When we have an implicit relation, we often assume that each variable can be written in terms any 2 others.


## S4. Where does V go?

I would also like to point out something strange. When you plug in $V = g(T, S)$ into $P = f(V, T)$ then the dependence of $P$ on $V$ disappears. 

Where does $V$ go? Why doesn't $P$ become a function of all of $T$, $S$, $V$?

Intuitive answer: by the state postulate, $P$ *cannot be* a function of those 3 variables - because then it would be **overconstrained**. Then, for arbitrary 3 variables, you can't expect that point to stay on a 2D manifold. I hope you see how critical the state postulate is!



- Wikipedia -- [Implicit Function Theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem)
- Wikipedia -- [State postulate](https://en.wikipedia.org/wiki/State_postulate)

- Wikipedia -- [Conjugate variables (thermodynamics)](https://en.wikipedia.org/wiki/Conjugate_variables_(thermodynamics))