---
id: thin
title: A smoothed prime sum is very small far out
kind: theorem
decl: QH.thin
module: Development.AutomorphicArithmetic.MeanSquareBounds.Thin
covers: 361
status: drafted
drafted_by: writer@claude
---
This theorem bounds a smoothed sum of $\Lambda(n)\chi(n)$ for a primitive [[Dirichlet character|JR4QSEFXWF]] $\chi$, at points $y$ that are very large compared with the conductor. Its user is [`thinH`](/entry/thin-h/), which applies it with $A = 2$ and $c = 1$. The analytic input is the prime number theorem for $\chi$ of [`psi_thin`](/entry/psi-thin/). This theorem only integrates that bound. Below it are 361 declarations.

## Statement

Let $\Lambda$ be the [[von Mangoldt function|087EMZTHWN]] and $\gamma$ the Euler constant. For a character $\chi \ne 1$ put

$$G_0(\chi, y) = \sum_{n \le y} \Lambda(n)\chi(n)\Bigl(\frac{y}{n} - 1\Bigr) + y\,\frac{L'(1,\chi)}{L(1,\chi)},$$

and for $\chi = 1$ put $G_0(1, y) = \sum_{n \le y} \Lambda(n)(y/n - 1) - y(\log y - 1 - \gamma)$. Say that $\chi$ has no zero near 1 with constant $c_0$ (`NoExc`) if $L(\beta,\chi) \ne 0$ for all real $\beta \in (1 - c_0, 1)$.

**Theorem.** Let $\varepsilon, A, c, c_0 > 0$. There is $x_0$ with this property. Let $x \ge x_0$. Let $\chi$ be a primitive character of modulus $N$ with $\log N \le A x^{\varepsilon/5} \log^2 x$. If $\chi$ is real and $\chi \ne 1$, suppose that $\chi$ has no zero near 1 with constant $c_0$. Then for all $y \ge \tfrac13 \exp(x^{\varepsilon/3})$,

$$|G_0(\chi, y)| \le y \exp\bigl(-c\, x^{\varepsilon/8}\bigr).$$

## Proof

Let $\psi_0(\chi, u) = \sum_{n \le u} \Lambda(n)\chi(n) - \delta_\chi u$, with $\delta_\chi = 1$ for $\chi = 1$ and $0$ otherwise. Partial summation gives $\sum_{n \le y} \Lambda(n)\chi(n)(y/n - 1) = y\int_1^y \psi(\chi,u)\,u^{-2}\,du$. The integral $\int_1^\infty \psi_0(\chi,u)\,u^{-2}\,du$ is $-L'(1,\chi)/L(1,\chi)$ for $\chi \ne 1$ and $-1-\gamma$ for $\chi = 1$. Together:

$$G_0(\chi, y) = -y \int_y^\infty \frac{\psi_0(\chi, u)}{u^2}\,du \qquad (y \ge 1).$$

In Lean this is `g_integral`. Put $\lambda = \max(1, \log N)$. [`psi_thin`](/entry/psi-thin/) gives $|\psi_0(\chi,u)| \le C u (\log u + \lambda)^2 \exp(-c_1 \log u / (\lambda + \sqrt{\log u}))$. For $u \ge y$ we have $\log u \ge x^{\varepsilon/3} - \log 3$, while $\lambda \ll x^{\varepsilon/5}\log^2 x$. So the exponent is at least about $x^{2\varepsilon/15}/\log^2 x$, which beats $c\,x^{\varepsilon/8}$ for each fixed $c$. The lemma `int_thin` does this integral. The theorem takes $x_0 = \max(x_1, e, 3^{3/\varepsilon})$, with $x_1$ from `int_thin`. The rest is bookkeeping.

## In the Lean code

The theorem is in [Thin.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/Thin.lean#L10). It calls:

- `psi_thin`, in [PsiThin.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PsiThin.lean#L385);
- `int_thin`, in [IntThin.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/IntThin.lean#L169);
- `g_integral`, in [GIntegral.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/GIntegral.lean#L229).

$G_0$ and `NoExc` are in [PrimeSetTwoBounds.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PrimeSetTwoBounds.lean#L69). The constant $c$ in the conclusion is arbitrary, because $2/15 > 1/8$. The constant $c_0$ is used only to call `psi_thin`. A primitive character $\chi = 1$ has modulus $N = 1$, so the case $\chi = 1$ is the case of $\zeta$.
