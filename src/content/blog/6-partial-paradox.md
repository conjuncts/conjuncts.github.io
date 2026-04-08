---
title: 'Partial Derivative Paradox (3/3)'
pubDate: 'Apr 7 2026'
revDate: 'Apr 7 2026'
description: "A short and sweet version"
author: conjuncts
tags: ["math"]
---


$$\def\pdc#1#2#3{\left(\frac{\partial #1}{\partial #2}\right)_{#3}}
$$
$\def\dd#1#2{\frac{d#1}{d#2}}$
$\def\pd#1#2{\frac{\partial #1}{\partial #2}}$

*A concise physics notational paradox involving simple kinematics.*

Partial derivatives, despite their simplicity, have caused me much headache through a combination of [notational ambiguity](https://www.youtube.com/watch?v=mICbKwwHziI) and [missing definitions](/blog/3-partial/). I describe a simple paradox to explain why partial derivatives are horribly ambiguous.

## The Paradox

Total energy is the familiar sum of gravitational potential and kinetic energy:

$$
E = mgh + \frac{1}{2}mv^2   \tag{1}
$$

Clearly, $\pd{E}{v} = mv$.

Suppose, furthermore, that we have a free-falling object: $h = \frac{1}{2} gt^2 + v_0 t + h_0$. By taking $v = \dd{h}{t} = gt + v_0$ and solving for $t$, we obtain the familiar velocity-displacement kinematic equation:

$$
h = \frac{v^2 - v_0^2}{2g} + h_0   \tag{2}
$$

Plugging that into Equation 1 yields:

$$
E = \frac{1}{2}m(v^2-v_0^2) + mgh_0 + \frac{1}{2}mv^2
$$
$$
= mv^2 + mgh_0 - \frac{1}{2}mv_0^2  \tag{3}
$$

But now, if you take $\pd{E}{v}$, you get:

$$
\pd{E}{v} = 2mv
$$

which is different from the $\pd{E}{v} = mv$ calculated above!

## The Solution

The key to the paradox is that $\pdc{E}{v}{h} = mv$, but $\pdc{E}{v}{h_0, v_0} = 2mv$. **That is, $\pd{E}{v}$ depends on the choice of dependent and constant variables.**

Let's look at the exact functions involved. Equation 1 is described by a function (call it $q$)
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

The key part is that $E$ can refer to two different functions! -- either $q$ or $s$. 

When we calculated $\pd{E}{v}$ for Equation 1, we really found $\pdc{E}{v}{h} = \pd{q}{v} = mv$.

But when we calculated $\pd{E}{v}$ for Equation 3, we really found $\pdc{E}{v}{v_0, h_0} = \pd{s}{v} = 2mv$.

But if we were to follow the (very common) practice of assigning the function as the same variable, then **two very different functions get assigned the same name**: $E = E(v, h) = E(v, v_0, h_0)$! 

That is why $\pd{E}{v}$ alone is ambiguous. To be unambiguous, you have two options:
1. (Mathematics): Be explicit in the functions involved; do not let the variable ($E$) and the function share the same name.
2. (Physics/Thermodynamics): Use parenthetical notation.

In regards to parenthetical notation, I find it remarkable that the notation $\pdc{a}{b}{c}$ is almost never defined. It is rare for any textbook to discuss  the link between differentiating a variable (ie. $\pdc{E}{v}{h}$) and differentiating a function (ie. $\pd{q}{v}$). This often leads the reader to assume $\pdc{E}{v}{h}$ and $\pd{E}{v}$ are the same thing -- but that leads to terrible ambiguities as shown above.

To address this, I define the parenthetical partial derivative in [another post](/blog/3-partial).