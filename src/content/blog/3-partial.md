---
title: 'Notational Differences of Partial Derivatives In Thermodynamics'
pubDate: 'Aug 10 2025'
revDate: 'Apr 3 2026'
description: "A diatribe against how partial derivatives in thermodynamics are notated, why they can be immensely confusing for outsiders, and how you can decipher them"
author: conjuncts
heroImage: '../../assets/3-partial.svg'
tags: ["math"]
---

$$\def\pdc#1#2#3{\left(\frac{\partial #1}{\partial #2}\right)_{#3}}
$$
$\def\dd#1#2{\frac{d#1}{d#2}}$
$\def\pd#1#2{\frac{\partial #1}{\partial #2}}$

*An observation of how partial derivatives in thermodynamics are notated, inherent notational ambiguities, and why it can be confusing.*

# Introduction

When I was a student in introductory thermodynamics, I observed that thermodynamicists seem to use a completely different notation for partial derivatives. 

Instead of using the typical notation found in your math textbooks, which is to define function $f(x, y, z)$ to have the partial derivative $\pd{f}{x}$ which depends on the function $f$ and a variable $x$...

Thermodynamicists use parentheses, $\pdc{P}{T}{V}$, to indicate how the quantity (not function) P varies over T, while explicitly notating $V$, the variables kept constant. One may ask: "isn't notating the constant variable redundant?" (Answer: yes *and* no!)

This notational difference is almost never discussed. You will be hard pressed to find a definition of the parenthetical partial derivative (ie. $\pdc{P}{T}{V}$) in either a math textbook *or* a thermodynamics textbook. The assumption that the definition is the same as the typical partial derivative, $\pd{f}{x}$, is a common and implicit one, yet *very* incorrect. 

Notational subtleties (and subsequent misunderstandings) lead to traps and apparent contradictions. The heuristic argument of keeping certain variables constant is often applied ad-hoc and inconsistently in proofs, leading to frustration for students accustomed to mathematical rigor or notational consistency. The confusion can be cleared up with a clear definition of the parenthetical partial derivative, something which is often painfully missing in many texts.

## Pitfall 1 (P1)

Observe this consequence from the [3rd Maxwell Relation](https://en.wikipedia.org/wiki/Maxwell_relations):

$$
\Delta S(T, V_2) - \Delta S(T, V_1) = \int_{V_1}^{V_2} \pdc{P}{T}{V} dV
$$

*What does it mean* to integrate with respect to V, while keeping V constant‽

## Pitfall 2 (P2)

Throughout calculus, one is ingrained with the idea that treating the derivative as a fraction of differentials is unrigorous and coincidental. Yet proofs involving treatment of differentials are baked into introductory thermodynamics. For example, take the [triple product rule](https://en.wikipedia.org/wiki/Triple_product_rule) and an unnamed 4-quantity identity:

$$
\pdc{P}{T}{V} \pdc{T}{V}{P} \pdc{V}{P}{T} = -1
$$

$$
\pdc{U}{V}{T} = \pdc{U}{V}{P} + \pdc{U}{P}{V} \pdc{P}{V}{T}
$$

The two identities above are most commonly proved in textbooks with an informal differential argument, sometimes involving ad-hoc replacement of $dV$ with $\partial V$. A differential argument is (as of 2026) listed as the first proof of the triple product rule on Wikipedia. For this reason, introductory proofs of even very fundamental identities can be unconvincing.

# Definition

To help clear things up, let me offer a definition.

Definition 1. Let there be a function $f: \mathbb{R}^n \to \mathbb{R}$, which without loss of generality is written:

$$
P = f(x, y_2, \cdots, y_n)
$$


Then we write the *parenthetical partial derivative* as:

$$
\pdc{P}{x}{y_2, \cdots, y_n} := \pd{f}{x}
$$

----

But **more importantly**, if you see the quantity $\pdc{P}{V}{T}$, then that can be "**unraveled**" into the following:

1. We are working with 3D phase space $(P, V, T)$.
2. There is a **function**, $f$, that accepts the dependent variable (here, V) and all constant variables (here, T): that is, $f(V, T)$
3. We have the **implicit relation** $P = f(V, T)$
4. $\pdc{P}{V}{T} := \pd{f}{V}$

----

If you see multiple constant variables like $\pdc{P}{V}{T, N_1, \cdots, N_r}$

then you can assume $P = f(V, T, N_1, \cdots, N_r)$ in $(r+3)$-dimensional phase space.

----

If you see higher order partial derivatives like $\pdc{^2P}{V \partial T}{N_1, \cdots, N_r}$

Then you can assume $P = f(V, T, N_1, \cdots, N_r)$ in $(r+3)$-dimensional phase space.

----

Caveat. At times, it is not possible to construct a global function $f$ due to (for instance) non-injectivity. However, the implicit function theorem guarantees that such a function $f$ generally exists in a local neighborhood around a point in question, which usually suffices for analysis.

## Why a separate function? (Pitfall 3)

Why create a separate function $f$? Can't we let $P$ refer to both the quantity and the function?

The short answer: because $P$ can be described by **different functions** depending your choice of dependent variables, making $\pd{P}{V}$ **fatally ambiguous**.

Assume:
- P in terms of T and V (Eqn. 1)
- V in terms of T and S (Eqn. 2)
- (let $P = f(T, V)$ and $V = g(T, S)$)

When you substitute "plug in" your formula for V (Eqn. 2) into P (Eqn. 1), you get a new function of only T and S. 

$$
P = P(T, V) = P(T, g(T, S)) = P(T, S)
$$

From the perspective of function composition,

$$
P = f(T, V) = f(T, g(T, S)) = h(T, S)
$$

**What is $\pd{P}{T}$ ?** 

Is it $\pd{f}{T}$ or is it $\pd{h}{T}$? They are completely different!!

By applying our definition, we get $\pdc{P}{T}{V} = \pd{f}{T}$, which is completely not the same as $\pdc{P}{T}{S} = \pd{h}{T}$.

Depending on what is held constant, we refer to **completely different functions**. If we aren't careful, they both would share the same name "P"!

For thermodynamicists, parenthesicals are **not** redundant but rather convey **crucial** information that distinguish whether you are working with function $f$ or $h$.   

But in mathematics, parentheticals **are** redudant, because mathematicians are working with the function directly!

---

If we had named the function $f$ to also be $P$, we get the confusing:

$$
P = P(T, V) = P(T, g(T, S)) = P(T, S)
$$

It becomes a lot harder to remember that the function $P(T, V)$ (that is, $f$) is different from the function $P(T, S)$ (that is, $h$)!

---


As a result of simple function composition, and combined with the common practice of assigning the quantity the same name as the function, we get a dangerous (and rarely discussed) ambiguity of partial derivatives. Because the parenthetical partial derivative is so rarely defined, it is incredibly easy for a beginner to confuse the two. To resolve this, I recommend thinking about the problem through the underlying function: either $f$ and $h$.


## Revisiting the Integral

Recall Pitfall 1:

$$
\int_{V_1}^{V_2} \pdc{P}{T}{V} dV
$$

With a newfound perspective, the situation becomes clear. Instead of worrying about which variables we change and hold constant, we look past all of that at the underlying function $f$ itself.

Here, we simply say that $P = f(T, V)$. Now, we just want:

$$
\int_{V_1}^{V_2} \pd{f}{T} \mathrm{d} V
$$

Now, $\pd{f}{T} (T, V)$ is a function just like any other, so of course it can be integrated.

# Conclusion

Parenthetical partial derivative notation ultimately has its merits, especially when working with many dependent variables ([re: EpsilonDelta](https://www.youtube.com/watch?v=QFHSHhpbo00)), as is common in physics/thermodynamics.

However, I believe the fundamental problem is that the parenthetical partial derivative is rarely (if ever) *defined*. The assumption that the parenthetical partial derivative is the same creature as the simple mathematical partial derivative is a common one, yet misunderstandings can lead to subtle yet extraordinary errors. 

The notation leads to apparent contradictions and confusion in interpretation (Pitfall 1), where the idea of "variable held constant" seems to be subjective idea applied only under case-by-case circumstance.

The parenthetical partial derivative often obscures the *actual function* for which the partial derivative is being taken. Worsening the problem is that the distinction between the *quantity* and the *function* is rarely, if ever made. The two are often (almost always!) assigned the same name, but this can be tremendously ambiguous, demonstrated in Pitfall 3, and lead to completely different partial derivatives. 

This confusion can be resolved with a clear definition of the parenthetical partial derivative, and specifically, insight into the precise function which is being differentiated. 

I find it tragic that these subtleties are almost never discussed, and particularly rarely in introductory textbooks (which teach and address precisely the audience most likely to be unaccustomed and confused with these subtleties of notation.)


## Further Reading


Note: this ambiguity with compositions and partial derivatives has been previously been covered excellently by [EpsilonDelta](https://www.youtube.com/watch?v=QFHSHhpbo00) -- [twice](https://www.youtube.com/watch?v=mICbKwwHziI).


- YT (EpsilonDelta) -- [Ambiguity With Partial ∂ Notation, and How to Resolve It](https://www.youtube.com/watch?v=mICbKwwHziI)
- YT (EpsilonDelta) -- [They Use ∂ Differently in Math and Physics. Which is Better?](https://www.youtube.com/watch?v=QFHSHhpbo00)
- Wikipedia -- [Implicit Function Theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem)
- Wikipedia -- [State postulate](https://en.wikipedia.org/wiki/State_postulate)
- Wikipedia -- [Conjugate variables (thermodynamics)](https://en.wikipedia.org/wiki/Conjugate_variables_(thermodynamics))

Textbooks for learning thermo:
- Korestky, Milo D. -- [Engineering and Chemical Thermodynamics, 2ed](https://www.amazon.com/Engineering-Chemical-Thermodynamics-Milo-Koretsky/dp/0470259612), in my opinion a great introductory textbook
- Levine, Ira N. -- [Physical Chemistry, 6ed](https://archive.org/details/PhysicalChemistry6eByIraN.Levine), less recommended


Discussion about formalisms:
- [Physics SE](https://physics.stackexchange.com/questions/388318/how-exactly-is-the-formalism-of-thermodynamics-based-on-contact-geometry)
- Callen, Herber B. -- [Thermodynamics and an Introduction to Thermostatistics](https://www.amazon.com/Thermodynamics-Intro-Thermostat-2E-Clo/dp/0471862568)
