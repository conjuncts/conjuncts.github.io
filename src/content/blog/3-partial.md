---
title: 'Thermo Partial Derivatives Make No Sense'
pubDate: 'Aug 10 2025'
description: "A diatribe against how partial derivatives in thermodynamics are notated, why they can be immensely confusing for outsiders, and how you can decipher them"
author: conjuncts
heroImage: '../../assets/3-partial.svg'
tags: ["math"]
---

$$\def\pdc#1#2#3{\left(\frac{\partial #1}{\partial #2}\right)_{#3}}
$$
$\def\dd#1#2{\frac{d#1}{d#2}}$
$\def\pd#1#2{\frac{\partial #1}{\partial #2}}$

*A diatribe against how partial derivatives in thermodynamics are notated, why they can be immensely confusing for outsiders, and how you can decipher them*


# Introduction

Partial derivatives in thermodynamics make no sense.

Instead of using the notation everyone else does (which is to define  function $f(x, y, z)$ to have the partial derivative $\pd{f}{x}$ when $y$ and $z$ are held constant )...

Thermo people notate with parentheses, $\pdc{P}{T}{V}$, to indicate how P (a quantity, not necessarily a function) varies over T, while keeping V constant. 

But P often relates not just to T and V, but also S, $\mu$, and others. These variables (S, $\mu$) can indeed vary with V, and often you are allowed to vary these auxiliary variables. How does it make sense to hold V constant, but allow S (which can depend on V) to vary?

The problem is, textbooks and professors almost never teach the corresponding notation that you will find in a math textbook. This results in a frankly frustrating experience for someone inclined towards mathematical rigor. I will now showcase apparent pitfalls and contradictions.

# The Problem

## P1. The Big Problem


If you still don't believe this is a problem: here is a very real, practical example, a consequence from the [3rd Maxwell Relation](https://en.wikipedia.org/wiki/Maxwell_relations):

$$
\Delta S(T, V_2) - \Delta S(T, V_1) = \int_{V_1}^{V_2} \pdc{P}{T}{V} dV
$$

**How the hell** do you integrate with respect to V, while supposedly keeping V constant?

## P2. Unconvincing proofs

Take these identities (the [triple product rule](https://en.wikipedia.org/wiki/Triple_product_rule) and what I *affectionately* call the "4-quantity juggle")

$$
\pdc{P}{T}{V} \pdc{T}{V}{P} \pdc{V}{P}{T} = -1
$$

$$
\pdc{U}{V}{T} = \pdc{U}{V}{P} + \pdc{U}{P}{V} \pdc{P}{V}{T}
$$

They are often "proved" using arguments with differentials. This is very unconvincing to someone wishing for mathematical rigor.



## P3. A confusing standard

From the identities, the variable being held constant makes a **huge** difference in how you evaluate the partial derivative.

In comparison with the mathematical definition, in which constant variables are implicitly baked into the function, can be omitted, and are somewhat irrelevant; 

In thermodynamics, changing what is held constant **completely changes** the partial derivative.


## P4. Unstated Assumptions

Partial derivatives - for example $\pdc{P}{T}{V}$ - are often presented without any mention of the **actual function**: whether P can be even written in terms of T and V at all, or whether these functions actually exist or if 2 variables is enough (or too many) variables to uniquely determine the dependent variable, or whether the 3 variables are invertible as claimed - etc. 

Also, what is the domain of these functions? Does P accept 2, 3, or more variables? Are we working with $\mathbb{R}^2 \to \mathbb{R}$, or something completely different?

Maybe it's just me, but I feel like some important info has been left out.

# The Solution

## S1. Stated Assumptions

First, a **gigantic** assumption, unfortunately often unmentioned, is the [state postulate](https://en.wikipedia.org/wiki/State_postulate). This states that 2 independent variables are often enough to define a thermodynamic state. 

This means we often work with a 2D manifold in thermodynamic space (for instance, the PvT surface is indeed a surface.) Without this assumption, many problems seem ill-posed in the sense of having many or no solutions. More generally, the Gibbs phase rule can be used to to get the dimension.

Also note that in thermodynamics, it can often be assumed that **variables are interdependent**. So if we have P, V, T, assume that each can be written in terms of the other 2 - that all those functions exist.

## S2. My approach

Here is my proposal.

Whenever you see a parenthetical partial derivative - ie.

$$
\pdc{P}{V}{T}
$$

Then know that:

1. There is a **function**, $f$, that accepts the dependent variable (here, V) and all constant variables (here, T): that is, $f(V, T)$
2. We have the **implicit relation** $P = f(V, T)$
3. $\pdc{P}{V}{T}$ is really just $\pd{f}{V}$.


### Multiple variables held constant

If you see multiple constant variables

$$
\pdc{P}{V}{T, N_1, \cdots, N_r}
$$

then you can assume $P = f(V, T, N_1, \cdots, N_r)$

### Higher order partials

If you see higher order partial derivatives:

$$
\pdc{^2P}{V \partial T}{N_1, \cdots, N_r}
$$

Then you can assume $P = f(V, T, N_1, \cdots, N_r)$.




## S3. Why a separate function?

Why create a separate function f, and let $P$ refer to both the quantity and the function?

I'm so glad you asked.

Say you have:
- P in terms of T and V; 
- V in terms of T and S
- (let $P = f(T, V)$ and $V = g(T, S)$)

When you "plug in" your formula for V into P, you get a new function of only T and S. That is, 

$$
P = f(T, V) = f(T, g(T, S)) = h(T, S)
$$

The key conundrum is, **what is $\pd{P}{T}$ ??**

Is it $\pd{f}{T}$ or is it $\pd{h}{T}$? They are completely different!!

However, our framework now tells us that:

$$
\pdc{P}{T}{V} = \pd{f}{T}
$$

which is completely not the same as:

$$
\pdc{P}{T}{S} = \pd{h}{T}
$$

Depending on what is held constant, we refer to *completely different functions*! And if we aren't careful, they both would share the same name "P"!


Note: this ambiguity with compositions and partial derivatives has been previously been covered excellently by [EpsilonDelta](https://www.youtube.com/watch?v=QFHSHhpbo00) -- [twice](https://www.youtube.com/watch?v=mICbKwwHziI). I recommend!

## S4. Where does V go?

I would also like to point out something strange. When you plug in $V = g(T, S)$ into $P = f(V, T)$ then the dependence of $P$ on $V$ disappears. 

Where does $V$ go? Why doesn't $P$ become a function of all of $T$, $S$, $V$?

Intuitive answer: by the state postulate, $P$ **cannot be** a function of those 3 variables - because then it would be **overconstrained**. Then, for arbitrary 3 variables, you can't expect that point to stay on a 2D manifold. I hope you see how critical the state postulate is!


## S5. Proving the Triple Product Identity

I now prove the identities in the language of multivariable calculus.


(TL;DR: see [here](https://math.stackexchange.com/a/3452693/1537176))

Assume from the state postulate that $P, V, T$ are all functions of each other. Let $f, g, h: \mathbb{R}^2 \to \mathbb{R}$, differentiable, partials never $0$, and write:
$$
P = f(V, T) \\
V = g(P, T) \\
T = h(P, V)
$$

**Claim**.

$$
-1 = \pd{f}{T} \pd{g}{P} \pd{h}{V}
$$

Using S2, equivalently:

$$
-1 = \pdc{P}{T}{V} \pdc{V}{P}{T} \pdc{T}{V}{P} 
$$


**Proof**.

Like mentioned in S3, we may plug one function into the other. We must be careful in composing ($g: \mathbb{R}^2 \to \mathbb{R}$ has real-valued is $f$ takes 2 real numbers, so $f \circ g$ makes no sense.) Hence, define:

$$
g^*(P, T) = \begin{bmatrix}
g(P, T) \\
T
\end{bmatrix}
$$


Then observe
$$
P = f(V, T) = f(g(P, T), T) = (f \circ g^*)(P, T) = P
$$


Note that the composition is identically $P$, suggesting a dummy function that simply takes (P, T) to P; that is:
$$
k(P, T) = P
$$

Calculate Jacobians:



$$
J_k = \begin{bmatrix} \pd{k}{P} & \pd{k}{T} \end{bmatrix} = \begin{bmatrix} 1 & 0 \end{bmatrix}
$$

$f \circ g^* = k$, so From the Jacobian chain rule, we get: 
$$
J_f J_{g^*} = 
\begin{bmatrix}
\frac{\partial f}{\partial V} & \frac{\partial f}{\partial T}
\end{bmatrix}
\begin{bmatrix}
\frac{\partial g}{\partial P} & \frac{\partial g}{\partial T} \\
0 & 1
\end{bmatrix} = J_k = \begin{bmatrix}
1 & 0
\end{bmatrix}
$$

$$
\begin{bmatrix}
\pd{f}{V} \pd{g}{P} & \pd{f}{V} \pd{g}{T} + \pd{f}{T} \\
\end{bmatrix} = \begin{bmatrix}
1 & 0
\end{bmatrix}
$$

(noting that $\pd{g^*_2}{P} = \pd{T}{P} = 0$ and $\pd{g^*_2}{T} = \pd{T}{T} = 1$)

So we get two equations:
$$
\pd{f}{V} \pd{g}{P} = 1  \tag{1}
$$
$$
\pd{f}{V} \pd{g}{T} + \pd{f}{T} = 0  \tag{2}
$$

(1) states that:
$$
\pdc{P}{V}{T} = \pd{f}{V} = \frac{1}{\pd{g}{P}} = \frac{1}{\pdc{V}{P}{T}}
$$
So in general, we are allowed to "flip" (take the reciprocal of) partial derivatives.


Work on the 2nd equation:
$$
\pd{f}{V} \pd{g}{T} = -\pd{f}{T}
$$
$$
\underbrace{\pd{g}{P} \pd{f}{V}}_{1} \pd{g}{T} = -\pd{f}{T} \pd{g}{P}
$$

$$
\pd{g}{T} = -\pd{f}{T} \pd{g}{P}
$$

$$
1 = -\pd{f}{T} \pd{g}{P} \frac{1}{\pd{g}{T}}
$$

We now need to flip a derivative, that is, we need $(\pd{g}{T})^{-1} = (\pdc{V}{T}{P})^{-1} = \pdc{T}{V}{P} = \pd{h}{V}$. This is not exactly the same equality (1). But we can obtain the fixed equality by repeating the above process -- but instead of composing $f$ and $g$, compose $g$ and $h$.

Hence, 
$$
\pd{f}{T} \pd{g}{P} \pd{h}{V} = -1
$$

$\square$

### Future Directions

Now, I admit that there are some edge cases that I haven't fully resolved yet. For instance, what happens if any of the partial derivatives vanish? But then the triple product rule breaks down anyways, because then $0 = -1$. 

What for some $V$, $T$ there are multiple valid $P$? (No global inverse) Is there a way to prove the identity by considering an implicit relation on $P$, $V$ and $T$, rather than having to use an explicit one?

I suspect the way to go is the [implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem#Statement_of_the_theorem). But I'd have to rework the proof to work on $U \subset \mathbb{R}^2$.

### Further Reading

Luckily, it seems that people have indeed already done this work. I recommend especially the [first link](https://math.stackexchange.com/a/3452693/1537176), which offers a similar but more concise proof using the IFT.
- [stack exchange](https://math.stackexchange.com/questions/3452654/finding-relationship-using-the-triple-product-rule-for-partial-derivatives)
- [blog post](https://gioretikto.github.io/mat/multivariable_calculus/euler_identity.html)
- [EpsilonDelta](https://www.youtube.com/watch?v=QFHSHhpbo00)

## S6. Proving the "4-Quantity Juggle"



Assume from the state postulate that $U, P, V, T$ are all functions of 2 others. Assume $f, g, h: \mathbb{R}^2 \to \mathbb{R}$, differentiable, partials never 0, and write:
$$
U = f(P, V)
$$
$$
P = g(V, T)
$$
$$
U = h(V, T)
$$

**Claim**.

$$
\pdc{U}{V}{T} = \pdc{U}{V}{P} + \pdc{U}{P}{V} \pdc{P}{V}{T}
$$

Using S2, equivalently:

$$
\pd{h}{V} = \pd{f}{V} + \pd{f}{P} \pd{g}{V}
$$

**Proof**.

The proof is similar. First, note that combining 

$$
U = h(V, T) = f(P, V) = f(g(V, T), V)
$$

Construct:

$$
g^*(V, T) = \begin{bmatrix}
g(V, T) \\ V
\end{bmatrix}
$$

We get that $U = h(V, T) = (f \circ g^*)(V, T)$

Construct Jacobians:

$$
J_{g^*} = \begin{bmatrix}
\pd{g}{V} & \pd{g}{T} \\ \\
\pd{V}{V} & \pd{V}{T}
\end{bmatrix} = \begin{bmatrix}
\pd{g}{V} & \pd{g}{T} \\ \\
1 & 0
\end{bmatrix}
$$

$$
J_f = \begin{bmatrix}
\pd{f}{P} & \pd{f}{V}
\end{bmatrix}
$$

$$
J_h = \begin{bmatrix}
\pd{h}{V} & \pd{h}{T}
\end{bmatrix}
$$

Matrix multiply:

$$
J_f  J_{g^*} = J_h
$$

$$
J_f = 
\begin{bmatrix}
\pd{f}{P} & \pd{f}{V}
\end{bmatrix}
\begin{bmatrix}
\pd{g}{V} & \pd{g}{T} \\ \\
1 & 0
\end{bmatrix}
=
\begin{bmatrix}
\pd{h}{V} & \pd{h}{T}
\end{bmatrix}
$$

Combining:

$$
\pd{f}{P}\pd{g}{V}  + \pd{f}{V} = \pd{h}{V} \tag{1}
$$
$$
\pd{f}{P}\pd{g}{T} = \pd{h}{T} \tag{2}
$$

(1) is exactly the desired identity. $\square$

Note that (2) is simply the chain rule -- equivalently:

$$
\pdc{U}{P}{V} \pdc{P}{T}{V} = \pdc{U}{T}{V}
$$

### Future directions

I wrote up this proof because the typical one uses differentials - and unconvincingly, $\dd{P}{V}$ gets transformed to $\pdc{P}{V}{T}$ because "T is constant".


I couldn't find any literature that uses the inverse function theorem to also patch up this identity when no global inverse exists. But it feels like a promising idea.

## S7. Revisiting the Integral

Recall P1:

$$
\int_{V_1}^{V_2} \pdc{P}{T}{V} dV
$$

My proposal doesn't change any of the facts of P1. But it does change the perspective! Instead of worrying about which variables we change and hold constant, we simply and sanely look at the function.

Here, we simply say that $P = f(T, V)$. Now, we just want:

$$
\int_{V_1}^{V_2} \pd{f}{T} \mathrm{d} V
$$

Now, $\pd{f}{T} (T, V)$ is a function just like any other. Of course it can be integrated! 


We get rid of all this nonsense about constant/varying variables, and it all makes sense.

# Conclusion

I apologize for the clickbait. There isn't actually anything wrong in the mathematical content about how thermodynamics treats partial derivatives. (I would hope not.) 

I've bashed the notation quite a lot, but perhaps undeservedly: the notation does makes sense once you get the hang of it. And the notation does genuinely work better when you have many dependent variables ([re: EpsilonDelta](https://www.youtube.com/watch?v=QFHSHhpbo00)), as is common in physics/thermodynamics.

However, I do think the pedagogy could be improved tremendously. It's incredibly easy to skip and ignore the many assumptions and hoops you have to make to really understand these partial derivatives. It's also incredibly easy to ignore the connection to the partial derivative definition known to the rest of mathematics. I doubt that any introductory undergraduate textbook will decipher partial derivatives as thoroughly as outlined today, but I wish it weren't so!


## Additional gripes and future directions

My biggest gripe is that thermodynamics makes some huge assumptions that often go untaught. Here are the major ones:

- Not mentioning the state postulate.
    - PLEASE mention the state postulate.
    - The state postulate says that we often work with a 2D manifold in thermodynamic space.
    - For instance, the PvT surface is indeed a surface (2D manifold).
    - Without this assumption, many problems seem ill-posed in the sense of having many or no solutions.
    - More generally, the Gibbs phase rule can be used to to get the manifold dimension.
- When we have an implicit relation, we often assume that each variable can be written in terms any 2 others.
- Partial derivatives are often allowed to be zero, infinity, or undefined.

### Implicit Relations?

Here, I resolve my doubts using explicit parametrizations -- and assume that everything is interdependent and invertible. But this is quite restrictive. Perhaps an implicit approach makes more sense and is more powerful. I still haven't fully resolved these assumptions with edge cases / when they go wrong. 

I believe the way to go is the [Implicit Function Theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem), which connects an implicit relation with local parametrizations, fixing proofs when no global parametrization exists. However, I perhaps need to take Differential Topology or Geometry to grasp the nuances of this.

