---
title: Zarhin's trick over a valuation ring
decls:
  - PositivityTheory.PrwZar.principal_of_quasiInverse
  - PositivityTheory.PrwZar.zarhinStatement_of_dual_cube_qiR
  - PositivityTheory.PrwZar.zarhinStatement_of_dual_cube
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Zarhin's trick over a valuation ring

This section proves Zarhin's trick for abelian schemes over the valuation ring of an algebraically closed valued field: if $A$ carries a relatively ample line bundle, then $A$ is a direct factor, as a group, of a principally polarized abelian scheme, namely $(A \times_R A^{\vee})^4$. The proof uses two published results, the existence of the dual abelian scheme and the theorem of the cube, together with Lagrange's four square theorem. The result is the content of [Zarhin's trick](/entry/zarhin/) as the proof uses it, where it reduces statements about heights of abelian varieties to the principally polarized case. The background is [polarizations and Zarhin's trick](/learn/abelian-varieties/#polarizations-and-zarhins-trick) and [duality and the Poincaré bundle](/learn/abelian-varieties/#duality-and-the-poincar-bundle).

Throughout, $S$ is a scheme and $A$, $B$ are [[abelian schemes|JDDXZ89N33]] over $S$, that is, commutative group objects in schemes over $S$ that are smooth, proper and with connected geometric fibres ([abelian schemes](/learn/abelian-varieties/#abelian-schemes)). A homomorphism is a morphism over $S$ that respects the group laws. The set $\operatorname{End}(A)$ is a ring, and $[m]_A$ is multiplication by $m$. For a line bundle $L$ on $A$ we write $\Lambda(L)$ for the Mumford bundle $\mu^{*}L \otimes p_1^{*}L^{-1} \otimes p_2^{*}L^{-1}$ on $A \times_S A$, where $\mu$ is the group law and $p_1$, $p_2$ are the projections.

**Definition 2.2.1 (Dual pair).** Let $P$ be a line bundle on $A \times_S B$. A line bundle $M$ on $A \times_S T$, for an $S$-scheme $T$, is *additive* if its restriction along $(a a', t)$ is isomorphic to the tensor product of its restrictions along $(a, t)$ and $(a', t)$, for all points $a, a'$ of $A$ and $t$ of $T$ with values in the same $S$-scheme. We say that $(B, P)$ is a *dual* of $A$ if $P$ is additive, $P$ is trivial on $A \times 0$, and for every $S$-scheme $T$ and every additive line bundle $M$ on $A \times_S T$ there is a unique morphism $x : T \to B$ with $M \cong (1 \times x)^{*}P$.

Lean: `GlobalTheory.AbDual.IsDual`.

So $B$ represents the functor of additive line bundles, which is the functor of the dual abelian scheme $A^{\vee}$ ([[dual abelian scheme|HZXSESHC8P]]). If $(B, P)$ is a dual of $A$, we write $P^{\sigma}$ for the pullback of $P$ to $B \times_S A$ by the swap of factors.

**Definition 2.2.2 (Polarization).** Let $(B, P)$ be a dual of $A$. A homomorphism $l : A \to B$ is a *polarization* (with respect to $P$) if for every algebraically closed field $\Omega$ and every point $s : \operatorname{Spec}\Omega \to S$ there is a relatively ample line bundle $L$ on the fibre $A_s$ with
$$\bigl((1 \times l)^{*} P\bigr)\big|_{A_s \times A_s} \cong \Lambda(L).$$

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.Zarhin.IsPolarisation`.

This is the usual definition: $l$ is fibrewise the map $\phi_L : a \mapsto t_a^{*}L \otimes L^{-1}$ of an ample line bundle.

**Definition 2.2.3 (Principal class).** Let $X$ be an abelian scheme over $S$. A class $c \in \operatorname{Pic}(X \times_S X)$ is *principal* if its pullbacks along $x \mapsto (0, x)$ and $x \mapsto (x, 0)$ are $0$, and for every algebraically closed field $\Omega$ and every point $s : \operatorname{Spec}\Omega \to S$ there is a relatively ample line bundle $L$ on $X_s$ with $K(L)$ trivial and with $c|_{X_s \times X_s}$ equal to the class of $\Lambda(L)$. Here $K(L)$ is the kernel of $\phi_L$.

Lean: `GlobalTheory.IndefiniteRowSideFullHecke.ZeroSectionBase.IsPrincipalPol`.

**Definition 2.2.4 (Principally polarized abelian scheme).** A *principally polarized abelian scheme* over $S$ is an abelian scheme $X$ over $S$, smooth of some relative dimension $g$, with a line bundle $M$ that is rigidified along the zero section, symmetric ($[-1]^{*}M \cong M$), relatively ample, and with $K(M)$ trivial.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.PolAV`.

We now give the construction of Zarhin. Lagrange's theorem that every natural number is a sum of four squares gives, for $N = a^2 + b^2 + c^2 + d^2$, the integer matrix of left multiplication by the quaternion $a + bi + cj + dk$:
$$\alpha = \begin{pmatrix} a & -b & -c & -d \\ b & a & -d & c \\ c & d & a & -b \\ d & -c & b & a \end{pmatrix}, \qquad \alpha^{T}\alpha = \alpha\alpha^{T} = N \cdot 1.$$

**Proposition 2.2.5 (Zarhin's construction).** Let $A$, $B$ be abelian schemes over $S$, both smooth of relative dimension $g$. Let $P$ be a line bundle on $A \times_S B$ such that $(B, P)$ is a dual of $A$ and $(A, P^{\sigma})$ is a dual of $B$. Let $l : A \to B$ be a polarization, and assume that there are $m \geq 1$ and a homomorphism $\mu : B \to A$ with $\mu \circ l = [m]_A$ and $l \circ \mu = [m]_B$. Put $X = (A \times_S B)^4$. Then there is a principal class $c \in \operatorname{Pic}(X \times_S X)$.

Lean: `PositivityTheory.PrwZar.principal_of_quasiInverse`.

*Proof.* Take $N = 4m^2 - 1$ and $\alpha$ as above, with $\alpha^{T}\alpha = \alpha\alpha^{T} = (4m^2 - 1)\cdot 1$. Write a point of $X$ as $u = (x_1, \dots, x_4, y_1, \dots, y_4)$ with $x_i$ in $A$ and $y_j$ in $B$, and a second point as $u'$. Let $c$ be the class of
$$\begin{aligned} c(u, u') = {} & \sum_{i} 2\, P(x_i, l x'_i) + \sum_{i, j} \alpha_{ij}\bigl(P(x_i, y'_j) + P(x'_i, y_j)\bigr) \\ & + \sum_{i} 2\, P(\mu y_i, l \mu y'_i), \end{aligned}$$
where $P(a, b)$ is the pullback of $P$ along $(a, b)$ and we write the group $\operatorname{Pic}$ additively. Each term is additive in each variable and trivial when one variable is $0$, since $P$ is trivial on $A \times 0$ and on $0 \times B$ (the second because $(A, P^{\sigma})$ is a dual). So $c$ is trivial on $0 \times X$ and on $X \times 0$.

Fix a geometric point $s$ and a relatively ample $L$ on $A_s$ with $(1 \times l)^{*}P \cong \Lambda(L)$. On $X_s$ consider
$$L' = \bigotimes_{i} \bigl(L(x_i) \otimes L(-x_i) \otimes L(\mu y_i) \otimes L(-\mu y_i)\bigr) \otimes \bigotimes_{i, j} P(x_i, y_j)^{\alpha_{ij}}.$$
By the theorem of the cube, $\Lambda(L(x) \otimes L(-x))$ is $2\Lambda(L)$ in the variable $x$, and $\Lambda(P(x, y))$ is $P(x, y') + P(x', y)$. So $\Lambda(L') = c|_{X_s \times X_s}$. Identify $A^{\vee}$ with $B$ and $B^{\vee}$ with $A$ through $P$, and work in $\operatorname{Hom}(A, B) \otimes \mathbb{Q}$. Then $l$ is symmetric, $\mu = m\, l^{-1}$, and $\mu^{\vee} l \mu = m^2 l^{-1}$. The homomorphism $\phi_{L'} : X_s \to X_s^{\vee} = B^4 \times A^4$ has the block matrix
$$\Phi = \begin{pmatrix} 2l & \alpha \\ \alpha^{T} & 2m^2 l^{-1} \end{pmatrix}, \qquad \Psi = \begin{pmatrix} 2m^2 l^{-1} & -\alpha \\ -\alpha^{T} & 2l \end{pmatrix},$$
and $\Phi \Psi = 1$ and $\Psi \Phi = 1$, because $4m^2 - (4m^2 - 1) = 1$ and the integer matrix $\alpha$ commutes with the diagonal action of $l$. The entries of $\Psi$ are homomorphisms, since $2m^2 l^{-1} = 2m\mu$. So $\phi_{L'}$ is an isomorphism and $K(L')$ is trivial. The bundle $L'$ is ample: the upper left block $2l$ comes from the ample bundle $L(x) \otimes L(-x)$, and its Schur complement $2m^2 l^{-1} - \alpha^{T}(2l)^{-1}\alpha = \tfrac{1}{2} l^{-1}$ is the class of a positive multiple of a polarization, so the Riemann form of $\Phi$ is positive definite. Hence $c$ is principal. $\square$

**Theorem 2.2.6 (Zarhin's trick, with a quasi-inverse).** Assume the existence of dual abelian schemes and the theorem of the cube (stated below). Assume also the following property (Q). Let $C$ be an algebraically closed field, $v$ a valuation on $C$ with values in $\mathbb{R}_{\geq 0}$, and $R \subset C$ its ring of integers. For abelian schemes $A$, $B$ over $\operatorname{Spec} R$ that are smooth of relative dimension $g$, a line bundle $P$ such that $(B, P)$ is a dual of $A$ and $(A, P^{\sigma})$ is a dual of $B$, and a polarization $l : A \to B$, there are $m \geq 1$ and a homomorphism $\mu : B \to A$ with $\mu \circ l = [m]_A$ and $l \circ \mu = [m]_B$.

Then the following holds. Let $C$, $v$ and $R$ be as above. Let $A$ be an abelian scheme over $\operatorname{Spec} R$, and let $L$ be a relatively ample line bundle on $A$. Then there are a principally polarized abelian scheme $X$ over $\operatorname{Spec} R$ and homomorphisms $i : A \to X$ and $r : X \to A$ with $r \circ i = 1_A$.

Lean: `PositivityTheory.PrwZar.zarhinStatement_of_dual_cube_qiR`.

The two published inputs are these. *Dual abelian schemes*: for every abelian scheme $A$ over a scheme $S$ there are an abelian scheme $B$ and a line bundle $P$ on $A \times_S B$ such that $B$ is smooth of relative dimension $g$ whenever $A$ is, $(B, P)$ is a dual of $A$, and $(A, P^{\sigma})$ is a dual of $B$ ([the dual abelian scheme](/entry/dual-abelian-scheme/)). *The theorem of the cube*: for an abelian scheme $A$ over $S$, a line bundle $L$ on $A$ and points $a, b, c$ of $A$ with values in an $S$-scheme $T$, the bundle
$$\begin{aligned} & L(a + b + c) \otimes L(a + b)^{-1} \otimes L(a + c)^{-1} \otimes L(b + c)^{-1} \\ & \otimes L(a) \otimes L(b) \otimes L(c) \otimes L(0)^{-1} \end{aligned}$$
on $T$ is trivial (D. Mumford, *Abelian Varieties*, §10).

*Proof.* The ring $R$ is local, so $\operatorname{Spec} R$ is connected. By the theorem of the cube, $\Lambda(L)$ is additive in each variable. Let $(B, P)$ be the dual given by the first published input. By the universal property there is a unique $l : A \to B$ with $\Lambda(L) \cong (1 \times l)^{*}P$, and $l$ is a homomorphism since $\Lambda(L)$ is additive in the second variable. The scheme $A$ is smooth of some relative dimension $g$ over the connected base, and so is $B$. Since $L$ is relatively ample, $l$ is a polarization: on each geometric fibre the required bundle is $L$ itself. Property (Q) gives $m$ and $\mu$, and the [Proposition 2.2.5](/entry/principal-of-quasi-inverse/) gives a principal class $c$ on $X \times X$ for $X = (A \times B)^4$, which is an abelian scheme. From the dual, the cube theorem and $c$ one obtains a line bundle $M$ on $X$ that is rigidified, symmetric and relatively ample, with $K(M)$ trivial and $\Lambda(M)$ in the class $c$. So $(X, M)$ is principally polarized. Let $i : A \to X$ be $a \mapsto ((a, 0), 0, 0, 0)$ and $r : X \to A$ the projection to the first factor $A$. Both are homomorphisms and $r \circ i = 1_A$. $\square$

**Corollary 2.2.7 (Zarhin's trick).** Assume the existence of dual abelian schemes and the theorem of the cube. Let $C$ be an algebraically closed field with a valuation $v$ with values in $\mathbb{R}_{\geq 0}$, and let $R$ be its ring of integers. Let $A$ be an abelian scheme over $\operatorname{Spec} R$ with a relatively ample line bundle. Then there are a principally polarized abelian scheme $X$ over $\operatorname{Spec} R$ and homomorphisms $i : A \to X$, $r : X \to A$ with $r \circ i = 1_A$.

Lean: `PositivityTheory.PrwZar.zarhinStatement_of_dual_cube`.

*Proof.* This is the [Theorem 2.2.6](/entry/zarhin-statement-of-dual-cube-qi-r/) applied to property (Q), which holds over $R$. We recall the proof of (Q). On each geometric fibre $l$ is finite, flat and surjective, since it is the map $\phi_L$ of an ample bundle. So $l$ is finite and flat, and its kernel $F$ is a finite flat commutative group scheme over $R$. Some $n \geq 1$ kills $F$. Then $[n]_A$ vanishes on $\ker l$, so it factors as $[n]_A = \mu \circ l$ through the finite flat surjection $l$. Then $l \circ \mu \circ l = l \circ [n]_A = [n]_B \circ l$, and since $l$ is an epimorphism, $l \circ \mu = [n]_B$. $\square$

**Remark 2.2.8.** Zarhin's original statement is for abelian varieties over a field: for every abelian variety $A$, the abelian variety $(A \times A^{\vee})^4$ is principally polarized (Yu. G. Zarhin, A remark on endomorphisms of abelian varieties over function fields of finite characteristic, 1974). The form here is over a valuation ring, and the projection and the inclusion of the first factor express that $A$ is a direct factor of $X$ as a group scheme. It does not identify the principal polarization of $X$ with the matrix $\Phi$: it only states the existence of some principal polarization.

**Remark 2.2.9 (Formalization).** The hypotheses of the Theorem are `GlobalTheory.Published.DualAbelianScheme`, `GlobalTheory.Published.CubeTheorem` and `PositivityTheory.PrwZar.QuasiInverseR` ([QiDefs.lean](lean:Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/QiDefs.lean#L21)); the conclusion is `ZarhinStatement` ([ZarhinStatement.lean](lean:Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/ZarhinStatement.lean#L21)). The valuation ring is given as a ring $R$ with $C$ an $R$-algebra and $v$ having $R$ as its integers. The four square matrix is `exists_quat` (by `Nat.sum_four_squares`). The Mumford bundle $\Lambda(L)$ is `abelian₂`, whose definition (a linear combination of pullbacks of $L$) we did not unfold. The ampleness and the triviality of $K(L')$ in the Proposition are `relAmple_zb` and `kTriv_zb`; we did not open these proofs, and the matrix argument above is the mathematics behind them, not a transcript. The symmetric bundle $M$ comes from `SymB.symmetricBundle`. Property (Q) is proved by `quasiInverseR` ([QiIsMonHomIdPow.lean](lean:Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/QiIsMonHomIdPow.lean#L58)) from fibrewise finiteness of $l$ and the fact that finite flat subgroups are killed by some $n$.
