---
title: The congruence statement for odd rank
decls:
  - UpperTheory.Gal.Int.Cong.congFinG_of_ex
  - UpperTheory.Gal.Int.Cong.congFinOdd_of_ex
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The congruence statement for odd rank

This section ends the proof of the congruence statement for the parameters of Section 24, which [the limit corollary](/entry/lim-fin-odd-of/) of Section 25 needs. Section 31 reduced it to the step statement, and Section 30 proved the weight change statement. The step statement asks in addition that each $U'$ has type $\mathrm{Ty}_\ell$ at $w_0$. We get this type by approximating forms by forms that contain a cuspidal type at $w_0$. The results are [the congruence theorem for the lacunary weight](/entry/cong-fin-g-of-ex/) and [the congruence theorem for odd rank](/entry/cong-fin-odd-of-ex/).

We keep the notation of Sections 25 and 28 to 31. Two places $u, v$ are *apart* when they lie over different places of the maximal real subfield of $E$.

### Inputs

**Proposition 3.33.1 (Types at $w_0$).** Let $a \geq 1$ and $w_0 \mid \ell$.

1. *Cuspidal types.* For each neighbourhood $N$ of $1$ in $\mathrm{GL}_a(E_{w_0})$ and each $m_0 \geq 0$, there are $m \geq m_0$, an open compact subgroup $J \subset N$ without elements of finite order other than $1$, and a homomorphism $\theta$ from $J$ onto $\mathbb{Z}/\ell^m$, such that for each character $\chi \neq 1$ of $\mathbb{Z}/\ell^m$, every smooth irreducible $\sigma$ of $\mathrm{GL}_a(E_{w_0})$ with a vector $v \neq 0$ on which $J$ acts by $\chi \circ \theta$ is cuspidal.
2. *Twisting by a type.* Let $w_0$ be split, $K$ a level away from $w_0$, $W$ a weight, $J \subset \mathrm{GL}_a(E_{w_0})$ open and compact without elements of finite order other than $1$, and $\theta : J \to \mathbb{Z}/\ell^m$ a homomorphism. Let $P_\theta(U)$ say: there are $\chi \neq 1$ and $\varphi \in U$, $\varphi \neq 0$, fixed by $K$, with $R(x) \varphi = \chi(\theta(c_{w_0}(x))) \varphi$ for every $x \in G_{w_0}$ with $c_{w_0}(x) \in J$. Then for each algebraic form $f$ of weight $W$ fixed by $K_J$ there are $F \in \mathrm{part}_K(P_\theta)$ and $e : G \to \mathbb{C}$ with $\lVert \iota^{-1} e(g) \rVert \leq \lVert \ell \rVert^m$ and $f(v)(g) - F(v)(g) = e(g) f(v)(g)$ for all $v, g$.

Lean: `UpperTheory.Gal.Int.Cong.ellSt_holds` (also `UpperTheory.Gal.Int.Cong.EllSt`, `UpperTheory.Gal.Int.Cong.exists_ellType`, `UpperTheory.Gal.Gen.tyStep_holds`, `UpperTheory.Gal.Gen.TyStep`).

These facts are proved elsewhere in the development, and we take them as given.

**Lemma 3.33.2 (Embeddings over two places).** Let $\tau$ lie over the pair of $u$ and over the pair of $v$. Then $u$ and $v$ are not apart. Hence, if $\mu_\tau = \lambda_\tau$ for every $\tau$ not over the pair of $v'$, and $t$ is locally $\lambda$-integral with support in elements whose components at the places not apart from $v'$ are trivial, then $t$ is locally $\mu$-integral.

Lean: `UpperTheory.Gal.Int.Cong.intL_congr` (also `UpperTheory.Gal.Int.Cong.exists_of_overPair`).

*Proof.* If $\tau$ lies over the pair of $u$, then $\tau$ lies over a place $x$ that is not apart from $u$: either $x = u$, or $\tau \circ c$ lies over $u$ and $x$ is the conjugate of $u$. In the same way $\tau$ lies over a place $y$ not apart from $v$. An embedding lies over at most one place, since such a place is a maximal ideal contained in the prime ideal of the $z$ with $\lVert \iota^{-1} \tau(z) \rVert < 1$. So $x = y$, and $u$ and $v$ lie over the same place of the maximal real subfield. For the second claim, let $g$ be in the support of $t$ and $u \mid \ell$ with $c_u(g) \neq 1$. Then $u$ is apart from $v'$, so no $\tau$ over the pair of $u$ lies over the pair of $v'$, and $\mu_\tau = \lambda_\tau$ for these $\tau$. So $\lvert \mu \rvert_u = \lvert \lambda \rvert_u$, and the bound for $\lambda$ is the bound for $\mu$. $\square$

### The two theorems

**Theorem 3.33.3 (Congruences for the lacunary weight).** The congruence statement at generic places holds for the type $\mathrm{Ty}_\ell$, $(D_a)$-genericity with the generic polynomials, and the lacunary weight.

Lean: `UpperTheory.Gal.Int.Cong.congFinG_of_ex` (also `UpperTheory.Gal.Int.Cong.stepSt_of_ex`).

*Proof.* By [the corollary of Section 31](/entry/cong-fin-g-of-step/), it is enough to prove the step statement. Take its data: $a, w_0, v', K, K_v, K'$, a family $(t_j)$ of functions that are $\lambda$-integral and locally $\lambda$-integral and act on $K'$-fixed vectors by $\eta$, an embedding $\tau_0$ over $v'$, and $U$ of type $(\lambda, K')$.

*Weight.* The weight change theorem of Section 30 uses only local integrality. It shows that $(\iota^{-1} \eta_j(U))_j$ is polynomially approximated by the families $(\iota^{-1} \eta_j(U_1))_j$ for the $U_1$ of type $(\mu, K)$, where $\mu_\tau = \lambda_\tau$ unless $\tau$ lies over the pair of $v'$, and $\mu_{\tau_0}$ satisfies the gap condition. By part 2 of the lemma on polynomial approximation of Section 31, with $Q = 1$, it is enough to approximate each such family by the families of the $U'$ of type $(\mu, K)$ with type $\mathrm{Ty}_\ell$ at $w_0$. Such $U'$ satisfy all conditions of the step statement, with the same $\mu$.

*Density of the type.* Fix $U_1$ and $\mu$. We show that forms with type $\mathrm{Ty}_\ell$ at $w_0$ approximate the forms of weight $W_\mu$ fixed by $K$. Let $f$ be such a form and $\varepsilon > 0$. By smoothness (Section 28), $f$ is fixed by the $x \in G_{w_0}$ with $c_{w_0}(x)$ in some neighbourhood $N$ of $1$. Choose $m_0$ with $\lVert \ell \rVert^{m_0} < \varepsilon$, and take $m, J, \theta$ from item 1. An element of $K_J$ is a product $k x$ with $k \in K$, $x \in G_{w_0}$ and $c_{w_0}(x) \in J \subset N$ (Section 28), so $f$ is fixed by $K_J$. Item 2 gives $F$ and $e$ with $\lVert \iota^{-1} e(g) \rVert \leq \lVert \ell \rVert^m \leq \lVert \ell \rVert^{m_0} < \varepsilon$. A space $U'$ with $P_\theta(U')$ has type $\mathrm{Ty}_\ell$ at $w_0$, with the same $m, J, \theta$ and $\chi$, since item 1 makes every $\sigma$ that contains $\chi \circ \theta$ cuspidal. So $F \in \mathrm{part}_K(\mathrm{Ty}_\ell)$.

*Eigenvalues.* By the lemma above, each $t_j$ is locally $\mu$-integral, so the $t_j$ are framed for $W_\mu$ (Section 30). A vector fixed by $K$ is fixed by $K' \subset K$, so the $t_j$ act on $K$-fixed vectors by $\eta$. The approximation by eigenvalues (Section 31, item 2), applied to $U_1$ of type $(\mu, K)$ and the density just proved, gives the approximation of $(\iota^{-1} \eta_j(U_1))_j$ by the $(\iota^{-1} \eta_j(U'))_j$ for $U'$ of type $(\mu, K)$ with type $\mathrm{Ty}_\ell$. $\square$

**Lemma 3.33.4 (From generic places to the congruence statement).** Let $\mathrm{Ty}$, $\mathrm{Gen}$, $\mathrm{Wt}$ be parameters and $\mathrm{Rk}$ any condition on $a$. The congruence statement at generic places for $\mathrm{Ty}, \mathrm{Gen}, \mathrm{Wt}$ implies the congruence statement of Section 25 for $\mathrm{Rk}, \mathrm{Ty}, \mathrm{Gen}, \mathrm{Wt}$.

Lean: `UpperTheory.Gal.Int.Cong.CongUWG.congUW4`.

*Proof.* Clauses 1, 2 and 4 are the same. For clause 3, let $Z$ and $W$ be given, with $W$ above $\ell$. Apply the statement at generic places to $Z \cup W$ and $W$; both sets satisfy its conditions. It gives constants $c(w, n) \neq 0$ and an approximation by spaces $U'$ that are generic at $Z \cup W$, hence at $Z$ and at $W$. $\square$

**Theorem 3.33.5 (The congruence statement for odd rank).** The congruence statement of Section 25 holds for the parameters of Section 24: $a$ odd, the type $\mathrm{Ty}_\ell$, $(D_a)$-genericity and the lacunary weight.

Lean: `UpperTheory.Gal.Int.Cong.congFinOdd_of_ex` (also `UpperTheory.Gal.Int.Cong.ellSt_holds`).

*Proof.* This is the theorem for the lacunary weight, with the lemma above for $\mathrm{Rk}$ the condition that $a$ is odd. $\square$

**Remark 3.33.6 (Formalization).** The lemma from generic places, at [NotApartOfOverPair.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/NotApartOfOverPair.lean#L252), ignores $\mathrm{Rk}$, so the oddness of $a$ in [CongFinOddOfLvLac.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/CongFinOddOfLvLac.lean#L15) is not used. The two theorems take the weight change statement as a hypothesis, and Section 30 proves it. The step statement asks for $\lambda$-integral and locally $\lambda$-integral functions; the weight change statement only for locally integral ones. Item 1 of the proposition is `exists_ellType`, and we did not open its proof or that of item 2.

## Notes and references

The main line of Section 26 is step 5 of [the Galois row](/proof/galois-row/), and its theorem feeds [Theorem 3.18.4](/entry/rest/). The theta lift statement is proved in [the theta lift theorem](/entry/t-lift-k/). Sections 27 to 32 prove two inputs of the sections before the main line: Section 27 proves the cutting fact of Section 24, and Sections 28 to 32 prove the congruence statement that [the limit corollary](/entry/lim-fin-odd-of/) of Section 25 uses. That corollary feeds [the main line](/entry/core-all-of/).

The standard construction uses unitary Shimura varieties in all weights; here the input is weight one with a theta lift. The weight is then moved by $\ell$-adic congruences: Sections 29 and 30 multiply a form by an $\ell$-adic approximation of a matrix coefficient of large highest weight, and Section 28 makes the Satake parameters generic by raising the level at $w_0$. Section 27 uses the theorem of Sen on the Lie algebra of the image of a Hodge-Tate representation. The eigenvector lemma of Section 30 is an approximate, $\ell$-adic relative of the lemma of Deligne and Serre on eigenvectors modulo a prime.

- S. W. Shin, *Galois representations arising from some compact Shimura varieties*, Ann. of Math. 173 (2011), for odd rank.
- G. Chenevier and M. Harris, *Construction of automorphic Galois representations II*, Cambridge J. Math. 1 (2013), for all ranks and all places.
- C. M. Sorensen, *A patching lemma*, in *On the Stabilization of the Trace Formula*, International Press (2011).
- J.-P. Labesse, *Changement de base CM et séries discrètes*, in the same book, for the descent.
- H. Jacquet and J. A. Shalika, *On Euler products and the classification of automorphic forms II*, Amer. J. Math. 103 (1981), for strong multiplicity one.
- S. Sen, *Lie algebras of Galois groups arising from Hodge-Tate modules*, Ann. of Math. 97 (1973), 160 to 170, for Section 27.
- P. Deligne and J.-P. Serre, *Formes modulaires de poids 1*, Ann. Sci. École Norm. Sup. (4) 7 (1974), §6, for the lifting of eigenvectors.
