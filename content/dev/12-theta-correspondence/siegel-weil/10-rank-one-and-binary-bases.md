---
title: Rank one and binary bases
decls:
  - PositivityTheory.Rg.Base1.baseOne_of
  - PositivityTheory.Rg.Base1.baseOne
  - PositivityTheory.Rg.Base1.densEq
  - PositivityTheory.Rg.Mass.e1
  - PositivityTheory.Rg.Mass.oneVecBinary
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rank one and binary bases

This section proves the Siegel-Weil identity for measures in two small cases: a Hermitian form of rank one, and an anisotropic binary form with a $1 \times 1$ target. From the rank one case and a local mass fact it deduces, by an induction on the rank, the identity for every anisotropic form with a nondegenerate target of the same size. That identity writes a theta mean as a product of local densities, and it is the last input of [the nondegenerate comparison](/entry/whit-gen-eq/). The binary case is an input of the comparison for forms of size less than $n$.

We use the Gram fibre families and the theta measure of [the section on Gram fibres](/entry/local-stages/), and the Euler product measure and the nondegenerate Siegel-Weil property of [the singular case](/entry/sw-free-singular/). Let $E/F$ be a CM extension with conjugation $\sigma$, see [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms).

**Definition 4.10.1 (Local signs).** For a finite place $v$ of $F$ with norm $Nv$, put $e_v = -1$ if $F_v \otimes_F E$ is a field, and $e_v = 1$ otherwise. Put $c_v = (1 - e_v / Nv)^{-1}$. A number $\Lambda$ is a limit value if
$$\prod_v \bigl( 1 - e_v Nv^{-s} \bigr) \to \Lambda \quad (s \to 1^{+}).$$

For $v$ unramified in $E$, $e_v$ is the value at $v$ of the quadratic [[Hecke character|KPYFGB342X]] $\eta$ of $E/F$, so $\Lambda$ is the value $L(1, \eta)^{-1}$ up to finitely many factors, see [Hecke characters](/learn/class-field-theory/#hecke-characters).

**Definition 4.10.2 (Siegel-Weil property with constant).** Let $J$ be an $M \times M$ Hermitian matrix and $T$ an $n \times n$ Hermitian matrix over $E$. The Siegel-Weil property with constant holds for $(J, T)$ if, for every basis $b$ of $E/F$, every standard system of measures, every Haar measure $\mu$ on $U_J(\mathbb{A})$ with a fundamental domain $\mathcal{F}$, and all nondegenerate Gram fibre families $m_\infty$ and $m_v$ for the coordinate measures, there is $c \ge 0$ with two properties:

1. the theta measure of $\{X : \operatorname{gr}(X) = T\}$ is the Euler product of $(m_\infty(T), c_v m_v(T))$ with constant $c$;
2. $c = \Lambda / 2$ for every limit value $\Lambda$.

**Definition 4.10.3 (Local mass fact).** The local mass fact is the statement that for almost all finite places $v$, the Gram fibre measure of the standard lattice at a unit of $F_v$, for a $1 \times 1$ form, times $c_v$, is 1.

**Theorem 4.10.4 (Rank one from the local mass fact).** Assume the local mass fact. Let $J$ be a nondegenerate $1 \times 1$ Hermitian matrix over $E$, and let $T$ be a $1 \times 1$ Hermitian matrix with $\det T \ne 0$. Then the Siegel-Weil property with constant holds for $(J, T)$.

Lean: `PositivityTheory.Rg.Base1.baseOne_of`.

*Proof.* The proof assembles four statements about the theta measure of the sphere $\{X : J(X, X) = \beta\}$ in a line of $E$.

1. For each $\beta \ne 0$ the theta measure at $\beta$ is an Euler product with some constant $c$. This comes from a length formula, which uses the local mass fact.
2. If $\beta$ and $\beta'$ are both represented by $J$, then the Euler product at $\beta$ with constant $c$ gives the one at $\beta'$ with the same $c$. This comes from the scaling of the fibre measures under $X \mapsto x X$.
3. If the fibre measure at $\beta$ is nonzero at $\infty$ and at every $v$, then $J$ represents $\beta$. This is the Hasse principle for Hermitian forms.
4. If one constant $\kappa$ works for every $\beta \ne 0$, then $\kappa = \Lambda / 2$ for every limit value $\Lambda$. This is a counting argument: the residue at $s = 1$ of an idelic zeta integral, a ratio that removes the twist by $e_v$ at the cost of the product $\prod_v (1 - e_v Nv^{-s})$, an open subgroup of index 2 of the ideles made of $F^\times$ times norms, and an identity that writes the theta mean as $\kappa$ times an idelic theta series of a function that vanishes off that subgroup.

By (1), (2) and (3) one constant works for all represented $\beta$, and the Euler product is zero for the others. By (4) the constant is $\Lambda / 2$. $\square$

**Theorem 4.10.5 (Rank one).** Let $J$ be a nondegenerate $1 \times 1$ Hermitian matrix over $E$, and $T$ a $1 \times 1$ Hermitian matrix with $\det T \ne 0$. Then the Siegel-Weil property with constant holds for $(J, T)$.

Lean: `PositivityTheory.Rg.Base1.baseOne`.

*Proof.* The local mass fact holds: at almost all $v$ the fibre measure of the standard lattice at a unit is computed by a count of solutions modulo $v$, through the trace form coordinates and an integral over the units. Apply [rank one from the local mass fact](/entry/base-one-of/). $\square$

**Theorem 4.10.6 (Theta means as products of densities).** Let $M \ge 1$, let $J$ be a nondegenerate $M \times M$ Hermitian matrix over $E$ such that $J(x, x) = 0$ implies $x = 0$, and let $T$ be an $M \times M$ Hermitian matrix with $\det T \ne 0$. Let $\Phi = \Phi_\infty \otimes \bigotimes_v \Phi_v$ be a factorizable Schwartz function on $M$-tuples of adelic vectors, with $\Phi_v$ the indicator of the standard lattice at almost all $v$. Fix a Haar measure $\mu$ on $U_J(\mathbb{A})$ with a fundamental domain $\mathcal{F}$, a standard character $\psi$ and its self-dual measures. Then there are continuous densities $g_\infty$ and $g_v$ of the Gram map against $\Phi_\infty$ and $\Phi_v$ such that the product converges and
$$\begin{aligned} & \frac{2}{\mu(\mathcal{F})} \int_{\mathcal{F}} \sum_{\operatorname{gr}(X) = T} \Phi(h^{-1} X) \, dh \\ & \quad = g_\infty(T) \, \Lambda \prod_v c_v \, g_v(T) \end{aligned}$$
for every limit value $\Lambda$.

Lean: `PositivityTheory.Rg.Base1.densEq`.

*Proof.* We prove the Siegel-Weil property with constant for $(J, T)$ by induction on $M$, and then convert the Euler product of measures into the identity of densities. The case $M = 1$ is [the rank one theorem](/entry/base-one/). The induction uses four steps. The property is invariant when $J$ is changed by an isometry $J' = {}^t \bar g J g$, and when $T$ is changed by $T' = {}^t \bar g T g$. A step from rank $M$ to rank $M + 1$ splits off a line: after a change of basis, $J$ is the sum of a line and a form of rank $M$, and the theta measure fibres over the first coordinate. When $T$ is not represented by $J$, both sides vanish. The last two steps use the local masses at almost all places, which come from the local mass fact. The induction also uses the binary results below and a bound on the binary masses. The densities $g_\infty$ and $g_v$ are the densities of the Gram fibre measures against $\Phi_\infty$ and $\Phi_v$; a fact at the infinite place gives their continuity. Dividing the Euler product identity by the volume of $\mathcal{F}$ gives the formula. $\square$

**Theorem 4.10.7 (Binary forms).** Let $J$ be a nondegenerate $2 \times 2$ Hermitian matrix over $E$ that is anisotropic, in the sense that $J(x, x) = 0$ implies $x = 0$. Let $T$ be a $1 \times 1$ Hermitian matrix with $\det T \ne 0$. Then the nondegenerate Siegel-Weil property holds for $(J, T)$.

Lean: `PositivityTheory.Rg.Mass.e1`.

*Proof.* The structure is that of the rank one case. A vector length formula gives an Euler product at each $\beta \ne 0$ with some constant; it uses the cocompactness of $U_J(F) \backslash U_J(\mathbb{A})$, which holds since $J$ is anisotropic, and the local mass formula. The constant does not change under similitudes, and the Hasse principle shows that every $\beta$ with nonzero local fibre measures is represented. A counting formula fixes the constant to 1. It uses a test function, a formula for the left side obtained by equidistribution and cocompactness, and a formula for the right side obtained by a mean value formula, a counting bound and the local mass formula. $\square$

**Corollary 4.10.8 (Binary forms, second form).** Let $M = 2$ and let $J$ be a nondegenerate $M \times M$ Hermitian matrix over $E$ with $J(x, x) \ne 0$ for every $x \ne 0$. Let $T$ be a $1 \times 1$ Hermitian matrix with $\det T \ne 0$. Then the nondegenerate Siegel-Weil property holds for $(J, T)$.

Lean: `PositivityTheory.Rg.Mass.oneVecBinary`.

*Proof.* Substitute $M = 2$. The condition $J(x, x) \ne 0$ for $x \ne 0$ gives $x = 0$ when $J(x, x) = 0$, by contradiction. Apply [the theorem on binary forms](/entry/e1/). $\square$

**Remark 4.10.9 (Formalization).** The density theorem passes the local mass fact twice, once inside the rank one theorem and once directly ([BaseOneOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/BaseOneSide/BaseOneOf.lean#L30)). The sign $e_v$ is $-1$ when $F_v \otimes_F E$ is a field, so also at ramified places, where one expects 0; the same $e_v$ occurs on both sides ([WhitGenLowOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhitGenLowOf.lean#L130)). The two binary statements state anisotropy in two equivalent forms ([MeanVal.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/BinaryMassMeans/MeanVal.lean#L13)). The four inputs of the rank one proof come from wrappers that are not unfolded here, so the proof above follows their names.
