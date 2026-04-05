---
title: 'Proof of the Triple Product Rule'
pubDate: 'Aug 10 2025'
revDate: 'Apr 3 2026'
description: "Satisfying (to me) proofs of the Triple Product Rule and an unnamed 4-variable identity: two identities of 2D surfaces in 3D space"
author: conjuncts
heroImage: '../../assets/3-partial.svg'
tags: ["math"]
---

$$\def\pdc#1#2#3{\left(\frac{\partial #1}{\partial #2}\right)_{#3}}
$$
$\def\dd#1#2{\frac{d#1}{d#2}}$
$\def\pd#1#2{\frac{\partial #1}{\partial #2}}$

## Motivation

The triple product rule is normally stated as: 
$$
-1 = \pdc{P}{T}{V} \pdc{V}{P}{T} \pdc{T}{V}{P} 
$$

And it is normally "proved" using an informal argument involving differentials.

That proof is unconvincing for many reasons, but one reason is: what happens if a partial derivatives is zero? We get the nonsensical identity $0 = -1$. Can we pinpoint the precise conditions needed for the identity to hold?

The typical proof of the 4-quantity identity also uses differentials -- and unconvincingly, $\dd{P}{V}$ gets transformed to $\pdc{P}{V}{T}$ because "T is constant". Can we also amend that proof?

## Proof


(TL;DR: see [here](https://math.stackexchange.com/a/3452693/1537176))

Let $M$ be a $C^1$-differentiable 2D manifold (thermodynamic surface) in $(P, V, T) = \mathbb{R}^3$. Let some point $(p_0, v_0, t_0) = u \in M$ be given. 

From the definition of a manifold, for some open neighborhood $W$ near $u$, $M$ may be described as the solutions of $F(P, V, T) = 0$, where $F: \mathbb{R}^3 \to \mathbb{R}$ is a differentiable function. (Think of $F$ as an arbitrary implicit relation, like $P^2T + TV + V^3 \ln P= 0$.)

**Suppose, furthermore, that the gradient $\nabla F$ never has a zero component in $W$.** (In other words, we guarantee that partial derivatives never vanish.)

From the Implicit Function Theorem, we obtain an open neighborhood $U$ for which (because of the nonvanishing condition) any variable can be described as the graph of any other 2 variables: that is, we obtain $C^1$ functions $f, g, h: \mathbb{R}^2 \to \mathbb{R}$ such that the point $(P, V, T)$ lies on the thermodynamic surface $M \cap U$ if and only if

$$
P = f(V, T) \\
V = g(P, T) \\
T = h(P, V)
$$

**Claim**.

$$
-1 = \pd{f}{T} \pd{g}{P} \pd{h}{V}
$$

By [Definition 1](/blog/3-partial/#definition), that is exactly

$$
-1 = \pdc{P}{T}{V} \pdc{V}{P}{T} \pdc{T}{V}{P} 
$$


**Proof**.

Intuitively, if $g$ which takes $(P, T) \to V$ is substituted into $f$ which takes $(V, T) \to P$ to yield an overall function $(P, T) \to P$, then we expect that the overall function ignores $T$ and simply spits out $P$.

But we must be careful: $g: \mathbb{R}^2 \to \mathbb{R}$ is real-valued but $f$ takes 2 real numbers, so $f \circ g$ makes no sense. Hence, define:

$$
g^*(P, T) = \begin{bmatrix}
g(P, T) \\
T
\end{bmatrix}
$$


Then
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

We now need to flip a derivative, that is, we need $(\pd{g}{T})^{-1} = (\pdc{V}{T}{P})^{-1} = \pdc{T}{V}{P} = \pd{h}{V}$. This is not exactly the same equality (1). But we can obtain the fixed equality by repeating the above process -- but instead of composing $f$ and $g$, compose $g$ and $h$. We finally obtain

$$
\pd{f}{T} \pd{g}{P} \pd{h}{V} = -1
$$

### Further Reading

There are more concise proofs using the same approach. Notably:
- Math SE -- [Triple Product Rule](https://math.stackexchange.com/a/3452693/1537176)
- gioretikto.github.io -- [Triple Product Rule](https://gioretikto.github.io/mat/multivariable_calculus/euler_identity.html)

Both similarly demand the never vanishing partials condition.

## S6. Proving the Unnamed 4-Quantity Identity

Assume $M$ to be a $C^1$-differentiable 2D manifold (thermodynamic surface) in $(U, P, V, T) = \mathbb{R}^4$. 

Assume that $M$ can be described (within an open neighborhood $W$ around point $u \in M$) with the functions $f, g, h: \mathbb{R}^2 \to \mathbb{R}$, differentiable, where 
$$
U = f(P, V)
$$
$$
P = g(V, T)
$$

if and only if $(U, P, V, T)$ is on the thermodynamic surface ($M \cap W$).

**Claim**.

$$
\pdc{U}{V}{T} = \pdc{U}{V}{P} + \pdc{U}{P}{V} \pdc{P}{V}{T}
$$

That is equivalent under [Definition 1](/blog/3-partial/#definition) to:

$$
\pd{h}{V} = \pd{f}{V} + \pd{f}{P} \pd{g}{V}
$$

where $h$ is defined as

$$
h(V, T) := f(g(V, T), V) = f(P, V) = U
$$

**Proof**.

The proof is similar. First, construct

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

(1) is exactly the desired identity.

(2) is simply the chain rule -- equivalently:

$$
\pdc{U}{P}{V} \pdc{P}{T}{V} = \pdc{U}{T}{V}
$$

### Future directions

You will occasionally have functions $f$ and $g$ simply by construction. But it would be nice to find some guarantee of $f$ and $g$ using the Inverse Function Theorem. 

Here, partial derivatives are allowed to be zero with no issue.

## References

- Triple product rule (AKA cyclic chain rule)
    - Math SE -- [proof with Implicit Function Theorem](https://math.stackexchange.com/a/3452693/1537176)
    - Math SE (Shifrin) -- [another proof](https://math.stackexchange.com/questions/3509203/why-is-the-cyclic-relation-of-partial-derivatives-correct)
    - Math SE (Shifrin) -- [further discussion](https://math.stackexchange.com/questions/2282799/where-does-the-relative-sign-come-from-in-this-chain-rule-application/2282804#2282804)
    - Math SE -- [further discussion](https://math.stackexchange.com/questions/4352876/clarification-about-the-triple-product-identity-for-partial-derivatives?noredirect=1&lq=1)
    - A [blog post](https://gioretikto.github.io/mat/multivariable_calculus/euler_identity.html)
    - Wikipedia -- [Triple Product Rule](https://en.wikipedia.org/wiki/Triple_product_rule)





## Acknowledgment

This article is substantially revised from an article originally released Aug 10 2025. 