---
title: Bernstein's Theorems A and B
decls:
  - PositivityTheory.RgUd.All.thmT
  - PositivityTheory.RgUd.AB.Final.thmA
  - PositivityTheory.RgUd.All.thmB
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bernstein's Theorems A and B

This section turns the vanishing theorem of the last two sections into two statements about the mirabolic subgroup. Theorem A says that a distribution on $\mathrm{GL}_{n+1}(k)$ that is invariant under conjugation by the mirabolic subgroup is invariant under conjugation by the whole group. Theorem B says that an irreducible [[unitary representation|74BPYJNZTM]] of $\mathrm{GL}_{n+1}(k)$ has, up to a scalar, only one sesquilinear form invariant under the mirabolic subgroup. Theorem B is the input of the [irreducibility theorem](/entry/bern-at/) for the step [EveryCharacter](/step/every-character/), through the derivatives of [Section 7.6.3](/entry/u-lift/).

Background: [smooth representations of $p$-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups), [generic representations](/learn/representations/#generic-representations-and-local-factors).

### Theorem T over every local field

Let $k$ be a nonarchimedean local field. Recall the vanishing property $(\mathrm{V}_Z)$ of [Section 7.2.2](/entry/t-final-thm-t/): every functional $\xi$ on the functions $M_n(k) \times k^n \to \mathbb{C}$ that is supported in $B_Z \times k^n$ and invariant on test functions under $(x, v) \mapsto (g x g^{-1}, g v)$ for $g \in G_Z$ kills every test function supported in $\{v \neq 0\}$.

**Theorem 7.4.1 (Theorem T).** For every $n$ and every commutative reduced subalgebra $Z \subseteq M_n(k)$, the property $(\mathrm{V}_Z)$ holds.

Lean: `PositivityTheory.RgUd.All.thmT`.

*Proof.* The characteristic of $k$ is $0$ or a prime $p$. In the first case apply [the theorem in characteristic zero](/entry/t-final-thm-t/). In the second case apply [the theorem in characteristic $p$](/entry/tp-final-thm-t/). $\square$

We use only the case $Z = k \cdot 1$. Then $B_Z = M_n(k)$ and $G_Z = \mathrm{GL}_n(k)$, and the support condition is empty. The theorem says: a distribution on $M_n(k) \times k^n$ that is invariant under $\mathrm{GL}_n(k)$ kills every test function that vanishes on $M_n(k) \times \{0\}$.

### Theorem A

Let $N = n + 1$, $G = \mathrm{GL}_N(k)$ and $M = M_N(k)$. Let $P \subseteq G$ be the *mirabolic subgroup*, the set of $g \in G$ with last row $e_N = (0, \dots, 0, 1)$. For a function $f$ on $G$ or on $M$ and $g \in G$, put $f^g(x) = f(g x g^{-1})$. A distribution $\Lambda$ is *$P$-invariant* if $\Lambda(f^p) = \Lambda(f)$ for all $p \in P$ and all test functions $f$, and *$G$-invariant* if this holds for all $p \in G$.

**Theorem 7.4.2 (Theorem A).** Assume Theorem T. Then every $P$-invariant distribution on $G$ is $G$-invariant.

Lean: `PositivityTheory.RgUd.AB.Final.thmA`.

The proof passes from $G$ to $M$, and then from $M$ to $M \times k^N$, where Theorem T applies.

**Proposition 7.4.3 (From $M$ to $G$).** Assume Theorem T, and assume that every $P$-invariant distribution on $M$ is $G$-invariant. Then every $P$-invariant distribution on $G$ is $G$-invariant.

Lean: `PositivityTheory.RgUd.AB.Pf.thmA_of_core`.

*Proof.* Let $\Lambda$ be $P$-invariant on $G$ and let $f \in S(G)$. The set $\det(\operatorname{supp} f)$ is compact and does not contain $0$. Choose a compact open set $U \subseteq k$ that contains it and does not contain $0$. For a function $\varphi$ on $M$, let $\varphi_U$ be the function on $G$ equal to $\varphi$ where $\det \in U$ and to $0$ elsewhere. Conjugation does not change the determinant, so $(\varphi^g)_U = (\varphi_U)^g$, and $\varphi \mapsto \Lambda(\varphi_U)$ is a $P$-invariant distribution on $M$. It is $G$-invariant by hypothesis. Apply this to the extension of $f$ by zero, whose cut is $f$ itself. $\square$

**Proposition 7.4.4 (Recovery).** Assume Theorem T. Let $\Lambda$ be a $P$-invariant distribution on $M$. Then there is a $G$-invariant distribution $L$ on $M$ with $L(f) = \Lambda(f)$ for all $f \in S(M)$.

Lean: `PositivityTheory.RgUd.AB.Pf.recover`.

*Proof.* For $w \in k^N$ with $w \neq 0$, choose $s_w \in G$ with last row $w$. For $F \in S(M \times k^N)$ put
$$\varphi_F(w) = \Lambda\big( x \mapsto F(s_w^{-1} x s_w, w) \big), \qquad \varphi_F(0) = 0.$$
Two choices of $s_w$ differ by left multiplication by an element of $P$, so $\varphi_F(w)$ does not depend on the choice, by the $P$-invariance of $\Lambda$. The function $\varphi_F$ is integrable, and we put $T(F) = \int_{k^N} \varphi_F(w)\, dw$. For $h \in G$ let $F_h(x, v) = F(h^{-1} x h, {}^t h v)$. A change of variables gives
$$T(F_h) = |\det h|^{-1}\, T(F).$$

Fix a nontrivial additive character $\psi$ of $k$ and let $\mathcal{F}$ be the Fourier transform in the variable $v$, with respect to $\psi$ and a [[Haar measure|VY0HXD3GC4]] on $k^N$. It is a bijection of $S(M \times k^N)$, and $\mathcal{F}(F_h)$ is $|\det h|^{-1}$ times $\mathcal{F}F$ composed with $(x, v) \mapsto (h^{-1} x h, h^{-1} v)$. Put $\xi = T \circ \mathcal{F}^{-1}$, and extend it linearly to all functions. The two factors $|\det h|^{-1}$ cancel, and $\xi$ is invariant under $(x, v) \mapsto (g x g^{-1}, g v)$ for all $g \in G$. By Theorem T with $Z = k \cdot 1$, $\xi$ kills every test function that vanishes on $M \times \{0\}$.

Let $B_0 \subseteq k^N$ be a compact open neighbourhood of $0$ and put $L(f) = \xi(f \otimes 1_{B_0})$ for $f$ on $M$. For $f \in S(M)$ and $g \in G$, the function $f^g \otimes 1_{B_0}$ and the translate of $f \otimes 1_{B_0}$ by $g$ agree on $M \times \{0\}$. So $\xi$ takes the same value on them, and $L$ is $G$-invariant.

It remains to show $L = \Lambda$ on $S(M)$. Let $f_0 \in S(M)$. Let $K_0 \subseteq G$ be a compact open subgroup with $f_0(k x k^{-1}) = f_0(x)$ for $k \in K_0$. For $w$ near $e_N$ we may take $s_w \in K_0$. So there is a small compact open neighbourhood $E$ of $e_N$ in $k^N$ on which $\varphi_F(w) = \Lambda(f_0)$ for $F = f_0 \otimes 1_E$. So $T(F) = \operatorname{vol}(E)\, \Lambda(f_0)$. At $v = 0$ the Fourier transform is the integral, so $\mathcal{F}F(x, 0) = \operatorname{vol}(E) f_0(x)$. The test functions $\mathcal{F}F$ and $(\mathcal{F}F)(\cdot, 0) \otimes 1_{B_0}$ agree on $M \times \{0\}$, so
$$\operatorname{vol}(E)\, L(f_0) = \xi\big((\mathcal{F}F)(\cdot,0) \otimes 1_{B_0}\big) = \xi(\mathcal{F}F) = T(F) = \operatorname{vol}(E)\, \Lambda(f_0).$$
Divide by $\operatorname{vol}(E) > 0$. $\square$

*Proof of Theorem A.* By the recovery proposition, a $P$-invariant distribution $\Lambda$ on $M$ agrees on test functions with a $G$-invariant $L$. So $\Lambda(f^g) = L(f^g) = L(f) = \Lambda(f)$. The first proposition then gives the theorem on $G$. $\square$

### Theorem B

Let $(\pi, V)$ be a smooth irreducible representation of $G$. A *sesquilinear form* on $V$ is a map $\beta : V \times V \to \mathbb{C}$, linear in the first variable and conjugate linear in the second. Let $B$ be an *invariant inner product*: a sesquilinear form with $B(w, v) = \overline{B(v, w)}$, $B(v, v) > 0$ for $v \neq 0$, and $B(\pi(g) v, \pi(g) w) = B(v, w)$ for all $g \in G$.

**Theorem 7.4.5 (Theorem B).** Assume Theorem A. Let $\beta$ be a sesquilinear form on $V$ with $\beta(\pi(p) v, \pi(p) w) = \beta(v, w)$ for all $p \in P$. Then $\beta = c B$ for some $c \in \mathbb{C}$.

Lean: `PositivityTheory.RgUd.All.thmB` (also `PositivityTheory.RgUd.AB.Final.thmB`).

The proof attaches a distribution on $G$ to each form.

**Proposition 7.4.6 (Trace distribution of a form).** Let $\pi$ be smooth, irreducible and admissible with an invariant inner product $B$. There is a linear map $\beta \mapsto D_\beta$ from sesquilinear forms on $V$ to distributions on $G$ with the following two properties.

1. If $\beta^g(v, w) = \beta(\pi(g) v, \pi(g) w)$, then $D_{\beta^g}(f) = D_\beta(f^{g^{-1}})$ for all $f \in S(G)$.
2. If $D_\beta(f) = 0$ for all $f \in S(G)$, then $\beta = 0$.

Lean: `PositivityTheory.RgUd.AB.Pf.formTraceDistrGL`.

*Proof.* For $f \in S(G)$, the operator $\pi(f) = \int_G f(g) \pi(g)\, dg$ has image in $V^K$ for a compact open subgroup $K$, and $V^K$ is finite dimensional by admissibility. Put $D_\beta(f) = \sum_i \beta(\pi(f) e_i, e_i)$, with $e_i$ a $B$-orthonormal basis of $V^K$ for $K$ small enough that $f$ is bi-invariant under $K$. The value does not depend on $K$. A change of variables gives property 1. For property 2, the operators $\pi(f)$ with $f$ bi-invariant under $K$ give every endomorphism of $V^K$, since $\pi$ is irreducible. So $D_\beta = 0$ forces $\beta = 0$ on each $V^K$, and $V$ is the union of these spaces. $\square$

*Proof of Theorem B.* An irreducible smooth representation of $\mathrm{GL}_N(k)$ is admissible, by the theorem of Jacquet and Bernstein. Let $\beta$ be $P$-invariant. By property 1, $D_\beta$ is $P$-invariant. By Theorem A it is $G$-invariant. So $D_{\beta^g} = D_\beta$ for all $g \in G$, and property 2 gives $\beta^g = \beta$. Now $\beta$ is a $G$-invariant sesquilinear form. On each $V^K$ there is an operator $A$ with $\beta(v, w) = B(A v, w)$. These operators fit together to an operator on $V$ that commutes with $\pi(G)$. By Schur's lemma for admissible irreducible representations, $A = c$, and $\beta = c B$. $\square$

**Remark 7.4.7.** Theorem B says that the restriction to $P$ of an irreducible unitarisable representation stays irreducible in the sense of forms. In [Section 7.6.3](/entry/u-lift/) it is used to show that the derivatives of an irreducible unitary representation carry invariant inner products.

**Remark 7.4.8 (Formalization).** The split by characteristic is in [BernAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/BernAll.lean#L13), and Theorem A is assembled in [ThmA.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TraceDistributionsGL/ThmA.lean#L13) from six facts about $\varphi_F$ and $T$ stated in [PhiIndep.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TraceDistributionsGL/PhiIndep.lean). Distributions are linear maps on all functions, and the invariance in Theorem A is asked only on test functions. The recovery proof applies Theorem T to the subalgebra of scalars, written as the bottom subalgebra ([IsLocallyConstantIndicatorOne.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TraceDistributionsGL/IsLocallyConstantIndicatorOne.lean#L131)). The section $w \mapsto s_w$ is a choice function with no continuity; only the independence of the choice is used. The cut by the determinant is in [MemSBIffSupportedIn.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TraceDistributionsGL/MemSBIffSupportedIn.lean#L65); it takes its extension by zero and its compact open set from a namespace with an unrelated name ([BoundOneTwo.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/BernsteinUnitaryProducts/BernsteinTheoremA/LeviTransposeDistributions/BoundOneTwo.lean)). Theorem B goes through the Kirillov form statement in [FormTraceDistrGL.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TraceDistributionsGL/FormTraceDistrGL.lean#L117). The statement of Theorem A for that route is defined twice, in [KirillovEndUnitaryOfTheoremA.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/BernsteinUnitaryProducts/BernsteinTheoremA/UnitaryKirillovModel/KirillovEndUnitaryOfTheoremA.lean#L257) and in [TheoremAOfLeviTranspose.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/BernsteinUnitaryProducts/BernsteinTheoremA/TheoremAFromLeviTranspose/TheoremAOfLeviTranspose.lean#L217).
