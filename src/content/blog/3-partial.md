---
title: 'Bugs in Thermodynamic Partial Derivative Notation (1/3)'
pubDate: 'Apr 3 2026'
revDate: 'Apr 7 2026'
description: "A diatribe against how partial derivatives in thermodynamics are notated, why they can be immensely confusing for outsiders, and how you can decipher them"
author: conjuncts
heroImage: '../../assets/3-partial.svg'
tags: ["math"]
---

$$\def\pdc#1#2#3{\left(\frac{\partial #1}{\partial #2}\right)_{#3}}
$$
$\def\dd#1#2{\frac{d#1}{d#2}}$
$\def\pd#1#2{\frac{\partial #1}{\partial #2}}$

*An observation of how partial derivatives in thermodynamics are notated, inherent notational ambiguities, and why they can be confusing.*

# Introduction

As a student in introductory thermodynamics, I observed that thermodynamicists use a completely different notation for partial derivatives. 

Instead of the typical notation found in math textbooks, which is to define function $f(x, y, z)$ to have the partial derivative $\pd{f}{x}$ which depends on the function $f$ and a variable $x$...

Thermodynamicists use parentheses, $\pdc{P}{T}{V}$, to indicate how the variable (not function) P varies over T, while explicitly notating $V$, the variables kept constant. One may ask: "isn't notating the constant variable redundant?" (Answer: yes *and* no!)

This notational difference is almost never discussed. You will be hard pressed to find a definition of the parenthetical partial derivative (ie. $\pdc{P}{T}{V}$) in either a math textbook *or* a thermodynamics textbook. The assumption that the definition is the same as the typical partial derivative, $\pd{f}{x}$, is a common and implicit one, yet *very* incorrect. 

Notational subtleties (and subsequent misunderstandings) lead to traps and apparent contradictions. The heuristic argument of keeping certain variables constant is often applied inconsistently in proofs, leading to confusion for students in want of rigor. The confusion can be cleared up with a clear definition of the parenthetical partial derivative, something often painfully missing in many texts.

## Pitfall 1 (P1)

Observe this consequence from the [3rd Maxwell Relation](https://en.wikipedia.org/wiki/Maxwell_relations):

$$
\Delta S(T, V_2) - \Delta S(T, V_1) = \int_{V_1}^{V_2} \pdc{P}{T}{V} dV
$$

*What does it mean* to integrate with respect to V, while keeping V constant‽

## Pitfall 2 (P2)

When working with parenthetical partial derivatives, we are instructed to differentiate along one dependent variable while holding others constant. What if the dependent variable relies on the constant variables? 

For instance, imagine $\pdc{P}{T}{V}$. It is entirely possible for temperature to depend on volume as well. What should one do?

## Pitfall 3 (P3)

Throughout calculus, one is ingrained with the idea that treating the derivative as a fraction of differentials is unrigorous and hazardous. Yet proofs involving manipulation of differentials are baked into introductory thermodynamics. For example, take the [triple product rule](https://en.wikipedia.org/wiki/Triple_product_rule) and an unnamed 4-quantity identity:

$$
\pdc{P}{T}{V} \pdc{T}{V}{P} \pdc{V}{P}{T} = -1
$$

$$
\pdc{U}{V}{T} = \pdc{U}{V}{P} + \pdc{U}{P}{V} \pdc{P}{V}{T}
$$

The two identities above are most commonly proved in textbooks with an informal differential argument, sometimes involving ad-hoc replacement of $dV$ with $\partial V$. A differential argument is, as of 2026, listed as the first proof of the triple product rule on Wikipedia. For this reason, introductory proofs of even fundamental identities can be unconvincing.

# Definition

To clear things up, let me offer a definition.

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

Caveat. At times, it is not possible to construct a global function $f$ due to non-injectivity, for instance. However, the implicit function theorem guarantees that such a function $f$ generally exists in a local neighborhood around a point in question, which usually suffices for analysis.

## Why a separate function? (Pitfall 4)

Why create a separate function $f$? Can't we let $P$ refer to both the variable and the function?

The short answer: because $P$ can be described by **different functions** depending your choice of dependent variables, making $\pd{P}{V}$ **fatally ambiguous**.

Assume:
- P in terms of T and V (Eqn. 1)
- V in terms of T and S (Eqn. 2)

When you substitute "plug in" your formula for V (Eqn. 2) into P (Eqn. 1), you get a new function of only T and S. 

$$
P = P(T, V) = P(T, V(T, S)) = P(T, S)
$$

**What is $\pd{P}{T}$ ?** 

Is it differentiating $P(T, V)$ or $P(T, S)$? Those two functions are completely different!

Let's take a step back and look at the underlying functions.
Let $P = f(T, V)$ and $V = g(T, S)$. From the perspective of function composition,

$$
P = f(T, V) = f(T, g(T, S)) = h(T, S)
$$

It becomes clear that $\pd{P}{T}$ can refer to either $\pd{f}{T}$ or $\pd{h}{T}$, which are completely different functions! By applying Definition 1, we get $\pdc{P}{T}{V} = \pd{f}{T}$, which is completely not the same as $\pdc{P}{T}{S} = \pd{h}{T}$.

For thermodynamicists, parentheticals are **not** redundant but rather convey **crucial** information that distinguish whether you are working with function $f$ or $h$. 

But in mathematics, parentheticals **are** redundant, because mathematicians are working with the function directly! 

And depending on what is held constant, the same name ($P$) can refer to **completely different functions**!


---

<details>
<summary>First example (ideal gas)</summary>


Consider an ideal gas with one mole:

**Equation 1:** $P = f(T, V)=\frac{RT}{V}$

This is the familiar ideal gas law ($PV = nRT$ with $n = 1$).

**Equation 2:** From the [entropy of an ideal gas](https://en.wikipedia.org/wiki/Ideal_gas#Entropy), one equation is:

$$S = R \ln \frac{VT^{c_V}}{n \Phi}$$


For simplicity, let $c_V = 2$, $n = 1$, and $\Phi = 1$, such that $S = R \ln (T^2V)$. After solving for $V$, we obtain
$$
V = g(S, T)=\frac{1}{T^2}\exp(S/R)
$$

By substituting Equation 2 into Equation 1, we get **Equation 3**:

$$
P = \frac{RT}{\frac{1}{T^2}\exp(S/R)} = \frac{RT^3}{\exp(S/R)}
= h(S, T) = f(T, g(S, T))
$$

**What is $\pd{P}{T}$?**

If we differentiate equation 1, then we get $\pdc{P}{T}{V} = \pd{f}{T} = \frac{R}{V}$. 

If we differentiate equation 3, then we get $\pdc{P}{T}{S} = \pd{h}{T} = \frac{2RT^2}{\exp(S/R)}$.

These are **completely different**!

Yet often the variable and function are given the same name, in which $\pd{P}{T}$ can refer to both $\pd{f}{T}$ and $\pd{h}{T}$. 

</details>

---


<details>
<summary>Second example (kinematics)</summary>

The next example comes not from thermodynamics, but from physics. Total energy is the familiar sum of gravitational potential and kinetic energy:

$$
E = mgh + \frac{1}{2}mv^2   \tag{1}
$$

Clearly, $\pd{E}{v} = mv$.

Suppose, furthermore, that we have a free-falling object.

$$
h = \frac{1}{2} gt^2 + v_0 t + h_0 \tag{2}
$$

By taking $v = \dd{h}{t} = gt + v_0$ and solving for $t$, we can derive the familiar velocity-displacement kinematic equation:

$$
h = \frac{v^2 - v_0^2}{2g} + h_0   \tag{3}
$$

Plugging that into Equation 1 yields:

$$
E = \frac{1}{2}m(v^2-v_0^2) + mgh_0 + \frac{1}{2}mv^2
$$
$$
= mv^2 + mgh_0 - \frac{1}{2}mv_0^2  \tag{4}
$$

But now, if you take $\pd{E}{v}$, you get:

$$
\pd{E}{v} = 2mv
$$

which is different from the $\pd{E}{v} = mv$ calculated above!

---

The key to the paradox is that $\pdc{E}{v}{h} = 2mv$, but $\pdc{E}{v}{h_0, v_0} = mv$.

We can also look at the functions involved. Equation 1 is described by a function (call it $q$)
$$
E = q(v, h) = mgh + \frac{1}{2}mv^2
$$

We then solved for $h$ in terms of $v$, which yielded a new function (call it $r$)

$$
h = r(v, v_0, h_0) = \frac{v^2 - v_0^2}{2g} + h_0
$$

When we substituted $h$ into Equation 1, we performed *function composition* to yield a new function $s$:

$$
E = q(v, h) = q(v, r(v, v_0, h_0)) =: s(v, v_0, h_0)
$$

The key part is that $E$ can refer to two different functions! -- either $q$ or $s$. If we were to follow the (very common) practice of assigning the function as the same variable, then two very different functions get assigned the same name: $E = E(v, h) = E(v, v_0, h_0)$.

Hence, when we calculated $\pd{E}{v}$ for Equation 1, we found $\pdc{E}{v}{h} = \pd{q}{v} = mv$.

But when we calculated $\pd{E}{v}$ for Equation 4, we found $\pdc{E}{v}{v_0, h_0} = \pd{s}{v} = 2mv$.

As you can see, $\pd{E}{v}$ alone is ambiguous. To be unambiguous, you have two options:
1. Use parenthetical notation.
2. Be explicit in the functions involved; do not let $E$ and the function share the same name.

</details>

---

As a result of simple function composition, and combined with the common practice of assigning the variable the same name as the function, we get a dangerous (and rarely discussed) ambiguity of partial derivatives. However, the confusion can be clarified by understanding the underlying functions $f$, $g$, and $h$.


## Revisiting the Integral

Recall Pitfall 1:

$$
\int_{V_1}^{V_2} \pdc{P}{T}{V} dV
$$

Definition 1 provides a newfound perspective. Instead of worrying about which variables we change and hold constant, we look past all of that and examine the underlying function $f$ itself.

We now know $P = f(T, V)$. Hence, we just want:

$$
\int_{V_1}^{V_2} \pd{f}{T} \mathrm{d} V
$$

Since $\pd{f}{T} (T, V)$ is a function just like any other, of course it can be integrated.

## Revisiting P2

If we have $\pdc{P}{T}{V}$ which implies existence of $P = f(T, V)$, **even if** $V$ depends on $T$ through some relation $V = g(T)$, that doesn't matter! 

Everything is still well-defined, since we know that $\pdc{P}{T}{V} = \pd{f}{T}$ for the function $f$ that takes both $T$ and $V$ as dependent variables. No need to worry about what happens after composition of $f$ with $g$.

## Revisiting P3

By connecting $\pdc{P}{T}{V}$ to the function $P = f(T, V)$, students can start to bridge thermodynamic identities with the theorems introduced in multivariable calculus. 

The proof of the triple product rule from is perhaps the most convincing evidence that Definition 1 is both valid and useful. However, this article is already long, so a proof of the triple product rule and 4-quantity identity is left to [another article](/blog/5-triple/).

# Conclusion

Parenthetical partial derivative notation has its merits, especially when working with many dependent variables (as is common in physics/thermodynamics).

But the fundamental problem is that the parenthetical partial derivative is rarely (if ever) *defined*. The assumption that the parenthetical partial derivative is the same creature as the simple mathematical partial derivative is a common one, yet misunderstandings lead to subtle yet extraordinary errors. 

It leads to apparent contradictions and confusions in interpretation (Pitfall 1), where the idea of "variable held constant" seems to be a subjective idea applied only under case-by-case circumstance.

It often **obscures the *actual function*** for which the partial derivative is being taken. Worse, the distinction between the *variable* and the *function* is rarely, if ever made. The two are often (almost always!) assigned the same name, but this can lead to great ambiguity and completely different partial derivatives, as discussed in Pitfall 4.

The confusion can be resolved with a clear definition of the parenthetical partial derivative.

So I find it tragic that the definition and its subtleties are almost never discussed, and particularly rarely in introductory textbooks -- which address precisely the audience most likely to be confused with these subtleties of notation.


## Further Reading


Ambiguity with function composition and partial derivatives has been excellently covered by [EpsilonDelta](https://www.youtube.com/watch?v=QFHSHhpbo00), [twice](https://www.youtube.com/watch?v=mICbKwwHziI).


- YT (EpsilonDelta) -- [Ambiguity With Partial ∂ Notation, and How to Resolve It](https://www.youtube.com/watch?v=mICbKwwHziI)
- YT (EpsilonDelta) -- [They Use ∂ Differently in Math and Physics. Which is Better?](https://www.youtube.com/watch?v=QFHSHhpbo00)

Textbooks for learning thermo:
- Korestky, Milo D. -- [Engineering and Chemical Thermodynamics, 2ed](https://www.amazon.com/Engineering-Chemical-Thermodynamics-Milo-Koretsky/dp/0470259612), in my opinion a great introductory textbook
- Levine, Ira N. -- [Physical Chemistry, 6ed](https://archive.org/details/PhysicalChemistry6eByIraN.Levine), less recommended


Discussion about formalisms:
- Physics SE -- [Contact Geometry?](https://physics.stackexchange.com/questions/388318/how-exactly-is-the-formalism-of-thermodynamics-based-on-contact-geometry)
- Callen, Herber B. -- [Thermodynamics and an Introduction to Thermostatistics](https://www.amazon.com/Thermodynamics-Intro-Thermostat-2E-Clo/dp/0471862568)

---

This article is substantially revised from an article originally released Aug 10 2025. 