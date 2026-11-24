---
title: Constant sections and the flat degree
decls:
  - GlobalTheory.CompanionTheory.Ar.Br.flatDegreeSt_of_resK_gaga
  - GlobalTheory.T.exists_const_section_kronecker_char
  - GlobalTheory.CompanionTheory.Ar.Br.CovEx.exists_constSec
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Constant sections and the flat degree

The bound of Proposition F in [the tower conditions](/entry/full-intersection-tower-i8-identity/) needs, on each component of the moduli space and for each CM type, a flat section of the line of that type, together with its arithmetic degree. This section proves the flat degree statement: such a flat section exists, and its degree is

$$
\frac{p - q}{2}\operatorname{Re}\log\Omega(E, \chi) + q\big(\log d_H - \log \mathrm{rd}_E\big),
$$

where $\chi$ is the Kronecker character of the host and $\log\Omega(E, \chi)$ is a Chowla-Selberg type period constant. The proof first builds a constant section with degree $\frac{p-q}{2}\operatorname{Re}\log\Omega(E, \chi)$ and then corrects it by a fixed defect at the finite places. The flat degree statement is used in [the next section](/entry/root-flat-on-hodge/) to build flat root lines of near record height.

We use the setting of [the chapter on good towers](/entry/good-tower-volume-of-reduced/): a CM field $E$ with host $H$ and prime discriminant $d_H$, a datum $D$ of signature $(p, q)$, a family $X_o$ of moduli spaces, a level $l$ and a coefficient field $c$ with field $F$. Let $U$ be a family of uniformizations, one for each embedding $\sigma \colon F \to \mathbb{C}$, with frames of rank $r$, and let $x \in \mathbb{R}$.

**Definition 9.8.1 (Laws of a uniformization).** The family $U$ satisfies the laws for $x$ if: $p + q \ge 1$; the level has $A = 1$ and is good at every prime; $U_\sigma$ is a uniformization at every good embedding; the function field of $X_o$ is algebraically closed in the sense of [the chapter on good towers](/entry/good-tower-volume-of-reduced/); the base points $\xi_0$ have norm $x$ under every embedding of $E$; the characters of the arithmetic groups are trivial on the lines of dominant weights and their matrices have determinant $1$; the cusp sections span the holomorphic sections in large degree; and there is a datum of signature $(1, 0)$.

**Definition 9.8.2 (Constant section).** Let $Z$ be a component, $\lambda$ a weight and $\delta$ a function on the finite places $\mathfrak{l}$ of $F$. A constant section for $(Z, \lambda, \delta)$ is a pair of rational sections $s$, $s'$ of the lines of weight $\lambda$ and $-\lambda$, supported on $Z$, with $s s' = 1$ on $Z$, together with:

1. constants $c_\sigma > 0$ such that the norm of $s$ under $U_\sigma$ is constant, equal to $c_\sigma$, on the frames over $Z$;
2. a function $\rho$ with finite support such that the valuation of $s$ at every point of $Z$ over $\mathfrak{l}$ is $\delta(\mathfrak{l}) + \rho(\mathfrak{l})$.

Its degree is

$$
\deg s = \sum_{\mathfrak{l}} \rho(\mathfrak{l})\, w(\mathfrak{l}) - \frac{1}{[F : \mathbb{Q}]}\sum_\sigma \log c_\sigma,
$$

with fixed weights $w(\mathfrak{l})$ of the places.

So a constant section is a section whose norm is constant at every place over $Z$; its degree is the arithmetic degree of the hermitian line it trivialises. For a CM type $\tau$ let $\lambda_\tau$ be the flat weight, with coefficient $-1$ at $\tau$ and $0$ elsewhere. The flat defect at $\mathfrak{l}$ is

$$
\delta_\tau(\mathfrak{l}) = q\big(\operatorname{ord}_{\mathfrak{l}}(\mathfrak{d}_\tau) - v_{\mathfrak{l}}(d_H)\big),
$$

with $\mathfrak{d}_\tau$ a conjugate different of the embedding of $\tau$. A flat section of type $\tau$ on $Z$ is a constant section for $(Z, \lambda_\tau, \delta_\tau)$. The weighted sum of the defects is

$$
\sum_{\mathfrak{l}} \delta_\tau(\mathfrak{l})\, w(\mathfrak{l}) = q\big(\log \mathrm{rd}_E - \log d_H\big).
$$

**Definition 9.8.3 (Flat degree statement).** For a Dirichlet character $\chi$ modulo $d_H$ put

$$
\log\Omega(E, \chi) = \gamma + \log\frac{2\pi}{\mathrm{rd}_E} - \frac{L'(1, \chi)}{L(1, \chi)},
$$

with $\gamma$ the Euler constant and $\mathrm{rd}_E$ the root discriminant. The character is a Kronecker character if $\chi(n)$ is the Jacobi symbol $\big(\frac{-d_H}{n}\big)$ for odd $n$. The flat degree value is

$$
\deg_{\flat}(D, \chi) = \frac{p - q}{2}\operatorname{Re}\log\Omega(E, \chi) + q\big(\log d_H - \log \mathrm{rd}_E\big).
$$

The flat degree statement says: for every host field, every Kronecker character $\chi$, and every family $U$ that satisfies the laws for some $x$, every component $Z$ and every CM type $\tau$ carry a flat section, and every flat section of type $\tau$ on $Z$ has degree $\deg_{\flat}(D, \chi)$.

The term $\frac{p-q}{2}\log\Omega$ is the shape of the Chowla-Selberg formula: the Faltings height of a CM abelian variety is a combination of logarithmic derivatives of $L$-functions at $s = 1$, and $\gamma + \log 2\pi$ comes from the gamma factor. Here the formula is taken as a result of the development through the frame bound below.

Two inputs from the top level inputs are used: the resolution statement for residue fields and the GAGA input for flat sections.

**Theorem 9.8.4 (Constant section with the Kronecker character).** Assume the resolution statement and the GAGA input. Let $U$ satisfy the laws for $x$, let $\chi$ be a Kronecker character modulo $d_H$, let $Z$ be a component and let $\tau$ be a CM type. Then there is a constant section $s$ for $(Z, \lambda_\tau, 0)$ with

$$
\deg s = \frac{p - q}{2}\operatorname{Re}\log\Omega(E, \chi).
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Br.CovEx.exists_constSec` (also `GlobalTheory.T.exists_const_section_kronecker_char`, a second name)

*Proof.* The section is built from an integral model and a flat line on it; its norms are read off at all places.

Choose an embedding of $F$ into $\mathbb{C}_2$. Since the level is good at $2$, there is a model of $X_o$ over a discrete valuation ring with good reduction. The component $Z$ is clopen and irreducible, and it gives a component $Z'$ of the model, which is geometric since the function field is algebraically closed.

The resolution statement and the GAGA input give a map $\varphi$ and a flat hermitian line of type $\tau$ on $Z'$. They also give the archimedean norms: for each good embedding $\sigma$ a number $t_\sigma$ such that the norm of the line on the frames over $Z$ is $t_\sigma$. An embedding $\sigma$ is either good or the conjugate of a good one, and the norm at a conjugate embedding is the same, so we get $t_\sigma$ for every $\sigma$.

At each prime $p$ and each embedding $F \to \mathbb{C}_p$, the frame function has a finite norm, and a local bound turns these norms into a function $\rho$ on the finite places. The existence of local valuation log norms gives adelic log norms $N$ with archimedean part $e^{t_\sigma}$ and finite part read from $\rho$. The frame bound for the Kronecker character says that $N$ is adelic and that its degree is $\frac{p-q}{2}\operatorname{Re}\log\Omega(E, \chi)$.

The flat line on the model gives rational sections $s$ and $s'$ on $Z$ with $s s' = 1$, which read the local heights of the line. The norm bound for uniformized sections at height $x$ gives that the norm of $s$ under $U_\sigma$ is constant, equal to $e^{t_\sigma}$, on the frames over $Z$; here the laws of $U$ are used. The valuation of $s$ at the points over $\mathfrak{l}$ is $\rho(\mathfrak{l})$. So $s$ is a constant section for $(Z, \lambda_\tau, 0)$, and its degree is the degree of $N$, which is the stated value. $\square$

**Theorem 9.8.5 (Flat degree statement).** The resolution statement and the GAGA input imply the flat degree statement.

Lean: `GlobalTheory.CompanionTheory.Ar.Br.flatDegreeSt_of_resK_gaga`

*Proof.* Let $U$, $x$, $\chi$, $Z$ and $\tau$ be given. By the previous theorem there is a constant section $s$ for $(Z, \lambda_\tau, 0)$ of degree $\frac{p-q}{2}\operatorname{Re}\log\Omega(E, \chi)$.

Change the defect of $s$ from $0$ to $\delta_\tau$, keeping the section and moving the difference into $\rho$; this is possible since $\delta_\tau$ has finite support. The result $t$ is a flat section of type $\tau$, and its degree changes by the weighted sum of the defects:

$$
\begin{aligned}
\deg t &= \deg s - \sum_{\mathfrak{l}} \delta_\tau(\mathfrak{l})\, w(\mathfrak{l}) \\
&= \frac{p - q}{2}\operatorname{Re}\log\Omega(E, \chi) + q\big(\log d_H - \log \mathrm{rd}_E\big) = \deg_\flat(D, \chi).
\end{aligned}
$$

So a flat section exists. Let $t'$ be any flat section of type $\tau$ on $Z$. Since the uniformizations are uniformizations at the good embeddings and the function field is algebraically closed, $t'$ is a nonzero constant multiple $a t$ with $a \in F$ and a nonzero constant multiple of a constant section has the same degree. So $\deg t' = \deg t = \deg_\flat(D, \chi)$. $\square$

The uniqueness part is what makes the flat degree a number attached to $(D, \chi)$ alone: it does not depend on the component, on $\tau$ or on the choice of section.

**Remark 9.8.6 (Formalization).** The flat degree statement asks that the host is a host field, but the proof does not use this hypothesis. The constant section theorem uses the prime $2$ for the model with good reduction. The flat degree statement is stated with the defect sum $q(\log\mathrm{rd}_E - \log d_H)$, and the sign bookkeeping happens in the rule for the degree after a change of defect ([FlatDegreeStOfResKGaga.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/FlatDegreeStOfResKGaga.lean#L18)). The second name is a statement file whose proof applies the first. We have not unfolded the weights $w(\mathfrak{l})$, the frame bound for the Kronecker character, the local norm statements, the GAGA input or the resolution statement; the reading of $\log\Omega$ as a Chowla-Selberg constant is ours.
