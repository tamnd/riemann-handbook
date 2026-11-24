---
title: Modularity of Hida families in rank three
decls:
  - UpperTheory.Gal.projectedFormsSystemPart.arithPointDecomposition_and_irrAutomorphic_of_isJ
  - UpperTheory.Gal.projectedFormsSystemPart.decomposition_and_automorphicAway_of_isJ
  - UpperTheory.V.Pa.has_automorphy_of_statement
  - UpperTheory.V.Z.J.D.modularity_n_of_printed_mult_comp
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Modularity of Hida families in rank three

This section proves that three-dimensional Hida families over a CM field are modular: for each universal ordinary determinant ring $B$ of rank three there is an ideal $J$ of $B$ such that the points of $B/J$ have the Hida properties of section 10, the two patching conditions, and the multiplicity comparison of section 18. The next section uses this statement as an input, and through it the counts I and V of section 1 depend on it. We keep the Hida setting, the unitary Hecke data and the ideals of Hecke type of section 18. The proof combines the Galois representations attached to points of Hecke type, a patching argument, and the multiplicity comparison.

**Theorem 8.19.1 (Points of Hecke type).** Assume the extended hypotheses. Let $J$ be an ideal of Hecke type. Then two statements hold.

1. (Decomposition.) Let $x$ be an arithmetic point of $B$ with $J \subseteq \ker x$. Then there is a continuous semisimple $\rho \colon G_L \to \mathrm{GL}_n(\overline{\mathbb{Q}}_l)$ attached to $x$, together with continuous representations $\rho'_i$ of dimensions $d_i \ge 1$ and integers $m_i \ge 1$, such that

$$\det(T - \rho(g)) = \prod_{i} \prod_{j=0}^{m_i - 1} \det\bigl(T - \rho'_i(g)\, \chi_{\mathrm{cyc}}(g)^{-j}\bigr)$$

for all $g$. If all $m_i = 1$, then at all but finitely many places $w$ any two Frobenius eigenvalues $z, z'$ of $\rho$ satisfy $|\iota z| < \mathrm{N}w \cdot |\iota z'|$.

2. (Automorphy.) Let $x$ be an arithmetic point with $J \subseteq \ker x$ and an irreducible attached representation $\rho$. Then $\rho$ is automorphic: it is attached through $\iota$ to a conjugate self-dual cuspidal representation, with the local conditions away from $v_0$.

Lean: `UpperTheory.Gal.projectedFormsSystemPart.decomposition_and_automorphicAway_of_isJ` (also `UpperTheory.Gal.projectedFormsSystemPart.arithPointDecomposition_and_irrAutomorphic_of_isJ`, the same statement with the link of projected forms as a hypothesis).

*Proof.* The extended hypotheses give the link between projected forms and Hida families. Let $x$ be arithmetic with $J \subseteq \ker x$. Then $x$ factors through $\mathbb{T}_K$, so it gives a Hecke eigensystem in the space of ordinary forms, and so an automorphic representation $\sigma$ of the unitary group. Base change from the unitary group to $\mathrm{GL}_n$ gives an isobaric sum of conjugate self-dual cuspidal representations, of the form $\boxplus_i (\pi_i \otimes |\cdot|^{\ast})$, with a segment of length $m_i$ for each $i$. The Galois representations of the $\pi_i$ are the $\rho'_i$, and the segments give the twists by powers of the cyclotomic character. This gives statement 1. When all $m_i = 1$ the base change is a sum of tempered pieces, and the weak purity bound comes from purity of each $\rho'_i$. When $\rho$ is irreducible there is one piece with $m_1 = 1$, and $\rho$ is attached to the cuspidal representation $\pi_1$, which gives statement 2. The integrality of the Hecke eigenvalues and the conjugation of the torsion at the places above $l$ make the attached representations continuous with values in $\overline{\mathbb{Q}}_l$. $\square$

**Definition 8.19.2 (Taylor-Wiles automorphy).** Let $J$ be an ideal of $B$. We say that $B$ has Taylor-Wiles automorphy for $J$ if for each Taylor-Wiles datum $T$ and each $N \ge 1$ there are a ring $A_N$ over the patched ring of $T$ and maps

$$\varphi \colon A_N \to B/J, \qquad \psi \colon B/J \to A_N,$$

with $\varphi \circ \psi$ equal to a fixed element and with two relations killed by the power $N!$.

This is the output of the Taylor-Wiles method in the form we use: the patched module relates $B/J$ to a ring that is finite and flat over a power series ring, up to a bounded error.

**Theorem 8.19.3 (Automorphy from patching).** Assume the local finiteness of Bernstein and Zelevinsky, the geometric lemma for Jacquet modules, and the tame local statement at the auxiliary primes. Let $J$ be an ideal of $B$ such that $B/J$ has a Taylor-Wiles base and, for each set of auxiliary primes, a classical module of forms of the auxiliary level. Then $B$ has Taylor-Wiles automorphy for $J$.

Lean: `UpperTheory.V.Pa.has_automorphy_of_statement`.

*Proof.* Lift the residual data to each auxiliary level. The local data at the auxiliary primes come from the tame local statement, and they give an action of the diamond operators on the classical modules. The finiteness of Bernstein and Zelevinsky and the geometric lemma show that the module of each auxiliary level is a finite module over the local ring at that level. The patching of these modules over $N$ gives operators on a patched module, and these transport to the ring $A_N$ and the maps $\varphi$ and $\psi$. $\square$

**Theorem 8.19.4 (Modularity of Hida families in rank three).** Assume the extended hypotheses. Let $L$ be a CM field with no primitive $l$-th root of unity, $s$ a Hida setting over $L$ with a level $V$ whose set of places is that of $s$, $\mathcal{O}$ a large coefficient ring, $r$ a residual representation of rank 3 with the condition at $v_0$, $B$ its universal ordinary determinant ring, $\Lambda$ a weight algebra and $\iota \colon \overline{\mathbb{Q}}_l \cong \mathbb{C}$. Then there is an ideal $J$ of $B$ such that $B/J$ has the Hida properties of section 10 (finiteness of the ring, density of arithmetic points, the point theorem, the decomposition and automorphy of its arithmetic points, and the twist condition), the two patching conditions, and the multiplicity comparison.

Lean: `UpperTheory.V.Z.J.D.modularity_n_of_printed_mult_comp`.

*Proof.* The extended hypotheses give unitary Hecke data for $r$ with no auxiliary primes, and an ideal $J$ of Hecke type. The [Theorem 8.19.1](/entry/decomposition-and-automorphic-away-of-is-j/) on points of Hecke type gives the decomposition and the automorphy of arithmetic points. The ring properties, the density and the twist condition come from the Hecke data. The [Theorem 8.19.3](/entry/has-automorphy-of-statement/) on patching gives Taylor-Wiles automorphy, and with local class field theory and the absence of $l$-th roots of unity this gives the two patching conditions. The density of arithmetic points makes $J$ radical, and the weight algebra of the Hecke data is a domain. So the [Theorem 8.18.8](/entry/num-j-prime-alt/) on multiplicity comparison applies, with the multiplicity of descents and the local matching proved above. $\square$

**Remark 8.19.5 (Formalization).** The multiplicity of descents and the local matching at split places are hypotheses of the modularity theorem but are theorems (`mult_free`, `compOf_free` in [CompOfFree.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/MultiplicityOne/CompOfFree.lean#L11)). The decomposition statement is `ArithmeticPointDecomposition` ([ArithmeticPointDecomposition.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AdmissibleResidues/ArithmeticPointDecomposition.lean#L26)); its weak purity bound quantifies over all pairs of Frobenius eigenvalues, so it includes $z = z'$. The modularity statement is the structure `ModularAlt` ([PointTheoremBaseObject.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PointTheoremBaseObject.lean#L39)), proved in [RadOfDense.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/RadOfDense.lean#L50). We have not unfolded the Taylor-Wiles data, `TWMaps`, the patching steps `opOf_alt` and `opToTW`, or the point theorem and the two patching conditions `P1core` and `P3core`.
