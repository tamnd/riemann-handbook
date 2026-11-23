---
id: gen-fe
title: The Godement-Jacquet functional equation with a partial L-function
kind: theorem
decl: UpperTheory.V.Z.Inf.genFE
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ArchimedeanSchwartz.GenericFunctionalEquation.GenFE
covers: 415
status: drafted
drafted_by: writer@claude
---
This theorem is the functional equation of the standard L-function of a cusp form on $\mathrm{GL}_n$, in the form of Godement and Jacquet (Zeta functions of simple algebras, Lecture Notes in Math. 260, 1972). It splits the global zeta integral into an archimedean zeta integral, local zeta integrals at a finite set $S$ of places, and the partial L-function outside $S$. It sits below [EveryCharacter from the Galois row](/step/every-character/). Its two users are `sideGCenOf` and `ImaginaryQuadraticEtaCharacter.sideXCen`.

## Statement

Let $K$ be a number field and $n \geq 2$. Let $\varphi_1, \varphi_2$ be cusp forms on $\mathrm{GL}_n(\mathbb{A}_K)$, with $\varphi_1$ invariant under the positive reals in the center. Let $f(g) = \int \varphi_1(xg)\overline{\varphi_2(x)}\,dx$ be their matrix coefficient, with $x$ in a fundamental domain for $\mathrm{GL}_n(K)$ in the norm-one adelic group, and suppose $f \neq 0$. Let $S$ be a finite set of finite places that contains the places dividing the different of $K$. For each finite $v$ let $\pi_v$ be an irreducible admissible representation, with smooth $\xi_v$ and smooth $\ell_v$ in the dual. For $v \notin S$, suppose that $\xi_v$ and $\ell_v$ are fixed by $\mathrm{GL}_n(\mathcal{O}_v)$, that $\ell_v(\xi_v) = 1$, and that $\pi_v$ has Satake parameter $z_v$. Suppose
$$f(g) = f_\infty(g_\infty) \prod_v \ell_v(\pi_v(g_v)\xi_v).$$
Let $\Phi_v$ be Schwartz-Bruhat on $M_n(K_v)$ for $v \in S$, and the indicator of $M_n(\mathcal{O}_v)$ for $v \notin S$.

**Theorem.** There are $c, c' \neq 0$ such that the Fourier transforms $\hat\Phi_v$ ($v \in S$) are Schwartz-Bruhat, and for each Schwartz function $\phi$ on $M_n(K_\infty)$ there are $\sigma \in \mathbb{R}$ and an entire $\Lambda$ such that for $\operatorname{Re} s > \sigma$, $L^S(s,\pi) \neq 0$ and
$$\Lambda(s) = c\, Z_\infty(\phi, f_\infty, s) \prod_{v \in S} Z(\Phi_v, f_v, s)\, L^S(s, \pi),$$
$$\Lambda(1-s) = c'\, Z_\infty(\hat\phi, \check f_\infty, s) \prod_{v \in S} Z(\hat\Phi_v, \check f_v, s)\, L^S(s, \tilde\pi).$$
Here $Z(\Phi, f, s) = \int \Phi(g) f(g) |\det g|^{s + (n-1)/2}\,dg$, $\check f(g) = f(g^{-1})$, $f_v$ is the local matrix coefficient, and $L^S(s,\pi) = \prod_{v \notin S} L(s, \pi_v)$.

## Proof

1. `GJGlobal.globalZeta_entire_functionalEquation` gives entire functions $\Lambda$, $\Lambda'$ with $\Lambda(s) = \Lambda'(1-s)$. They are the global zeta integrals of $\phi \otimes \bigotimes \Phi_v$ and of its Fourier transform.
2. `exists_unramified` shows that for $v \notin S$ the local zeta integral of the indicator is $L(s,\pi_v)$, for $\pi_v$ and for its contragredient, and that the products converge for large $\operatorname{Re} s$.
3. `globalZeta_eq_euler` factors the global integral as an Euler product. `exists_adelicMatrixFourier_matrixTensor` and `tensor_hyps_fourier` show that the adelic Fourier transform of the product is a constant $C$ times the product of the local transforms.
4. Take $c$ from the measure constants and $c' = Cc$. The partial L-function is a convergent product of nonzero factors, so it is not 0.

## In the Lean code

The theorem is in [GenFE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ArchimedeanSchwartz/GenericFunctionalEquation/GenFE.lean#L13). The definitions of $L^S$ and of $Z_\infty$ are in [GJStandardLDefs.lean](lean:GroundTheory/AutomorphicForms/GL2/GJStandardLDefs.lean#L119).

- Irreducibility and admissibility are assumed at all $v$, but the proof passes them on only for $v \notin S$ (line 48).
- "Ramified places" in Lean means the places that divide the different of $K$. They have nothing to do with $\pi$. The set $S$ need not contain the places where $\pi$ ramifies; the hypotheses on $\xi_v$, $\ell_v$ do that work.
- The second identity is written at $1-s$, so both hold on the same half plane.
