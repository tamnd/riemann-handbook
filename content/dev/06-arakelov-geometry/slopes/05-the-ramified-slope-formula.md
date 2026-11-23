---
title: The ramified slope formula
decls:
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_isometry
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_character_finite
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slopeLine_of_tied
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slopeLine_tied
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.slopeLine_0
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The ramified slope formula

The theorem of Section 4 proves the ramified slope formula under six conditions. This section shows that four of them follow from the compatible forms at level zero, together with one condition on the character of the level group. The result is the final form: under the Hida setting, compatible forms at level zero, and a level character of finite order with values in $K$, the ramified lattice has slope $\mu(A_0) - f\log(T-1)/(T-2)$. It is used in the restriction to the level prime in Volume 11, where the ramified part of the level-zero lattice is compared with the forms of level $T$.

We keep the setting of Section 4. Recall that $A_0 = (V, b, X, L)$ is the level-zero lattice over the totally complex field $K$, that $A_{\mathrm{ram}}$ is its ramified sublattice for the diamond action of $G = \prod_{v \in \mathfrak{v}_T} \mathbb{F}_v^\times$, and that the ramified slope formula is the identity
$$
\mu(A_{\mathrm{ram}}) = \mu(A_0) - f\, \frac{\log(T-1)}{T-2} .
$$

### Four consequences of compatible forms

We take the following four results from the chapters that construct the compatible forms. Each is a property of the explicit adelic description of the level-zero forms, and its proof lies outside this chapter.

**Proposition 1.5.1 (Properties of compatible forms at level zero).** Assume compatible forms at level zero. Then:

1. every level-zero class has trivial stabilizer;
2. the classes are orthogonal: if $x, y \in V$ and for every class $c$ one of $\varepsilon(x)(c)$, $\varepsilon(y)(c)$ vanishes, then $\langle x, y \rangle_v = 0$ for every infinite place $v$;
3. the CM extension splits at every place of $\mathfrak{v}_T$, in the sense of the corollary on split primes in Section 4.

Say that the *level character has finite order with values in $K$* if there is an $n > 0$ such that every value $\chi(x)$ of the character $\chi$ of the level group at level zero satisfies $\chi(x)^n = 1$ and lies in the image of $K$ in $\mathbb{C}$. If this holds and the stabilizers are trivial, then

4. the diamond operators $\rho(v, a)$ on $V$ preserve every majorant.

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.admissible_stabilisers_of_compatible_forms` (also `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.metric_disjoint_support_orthogonal`, `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.splitAtT_of_tied`, `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.diamond_isometry_at_infinity`).

*Proof.* We indicate the idea of each part and refer to the construction of the compatible forms for the details. For part 1, every element of the stabilizer of a class is mapped injectively into the level group, where the compatibility forces it to be trivial. For part 2, every form in $\varepsilon(V)$ is given class by class by a polynomial, and the majorant at $v$ is computed class by class in an orthonormal frame of the hermitian form at $v$; so two forms with disjoint supports are orthogonal. For part 3, the idempotent is built from an integral element $\pi$ attached to the place and its conjugate $\bar\pi$, through $\alpha = \pi - \bar\pi$, which satisfies $\bar\alpha = -\alpha$ and $\alpha^2 \in F$. For part 4, it suffices by polarization to show $\|\rho(v,a) x\|_w = \|x\|_w$ for all $x$ and every infinite place $w$, since $\rho(v,a)$ is $K$-linear and the majorant is sesquilinear for the embedding $\sigma_w$, which is not real because $K$ is totally complex. The norm identity is proved from the explicit frames at the infinite places, and this is where the finite order of the level character is used. $\square$

### The ramified slope formula

**Theorem 1.5.2 (Ramified slope formula from the diamond isometry).** Assume the Hida setting, compatible forms at level zero, trivial stabilizers, and that the diamond operators preserve every majorant. Then the ramified slope formula holds.

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_isometry`

*Proof.* By parts 2 and 3 of the proposition, the classes are orthogonal and the CM extension splits at every place of $\mathfrak{v}_T$. The corollary on split primes in Section 4, [Corollary 1.4.4](/entry/slope-formula-of-split/), now applies. $\square$

**Theorem 1.5.3 (Ramified slope formula for a character of finite order).** Assume the Hida setting, compatible forms at level zero, that the level character has finite order with values in $K$, and that the level-zero classes have trivial stabilizers. Then the ramified slope formula holds.

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_character_finite` (also `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slopeLine_of_tied`, the same statement in the form used in Volume 11).

*Proof.* By part 4 of the proposition, the diamond operators preserve every majorant. This is [Theorem 1.5.2](/entry/slope-formula-of-isometry/) applied with this isometry. $\square$

**Theorem 1.5.4 (Ramified slope formula).** Assume the Hida setting, compatible forms at level zero, and that the level character has finite order with values in $K$. Then
$$
\mu(A_{\mathrm{ram}}) = \mu(A_0) - f\, \frac{\log(T-1)}{T-2} .
$$

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.slopeLine_0` (also `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slopeLine_tied`).

*Proof.* By part 1 of the proposition the stabilizers are trivial, and [Theorem 1.5.3](/entry/slope-formula-of-character-finite/) applies. $\square$

### What the formula says

The number $f \log(T-1)/(T-2)$ does not depend on the weights, on the number of classes, or on the metric. It comes only from the combinatorics of the group $G$. The ramified lattice is a Kronecker image of $L_W^S$ with $S = \prod_v (\mathbb{F}_v^\times \setminus \{1\})$ of size $(T-2)^f$, and the Gram matrix of the change of variables has determinant $(T-1)^{f (T-2)^{f-1}}$. So the drop is the logarithm of this determinant divided by $|S|$. As $T \to \infty$ the drop is about $f \log T / T$, which tends to $0$: the ramified sublattice of a large level prime has almost the same slope as the whole lattice.

**Example 1.5.5.** The Hida setting forces $f \geq 2$ and $T > 5$, but the formula itself makes sense for any $f \geq 1$ and $T \geq 3$. Take $f = 1$ and $T = 3$. Then $G = \mathbb{F}_3^\times$ has two elements, the ramified lattice is the antidiagonal $\{x - \rho(g)x\}$ of the two summands of the slice decomposition, and its slope is $\mu(A_0) - \log 2$. This is the antidiagonal example of Section 2.

In the normalization of Volume 1, where slopes are half of ours, the formula reads $\widehat{\mu}(\overline{E}_{\mathrm{ram}}) = \widehat{\mu}(\overline{E}_0) - \frac{f}{2} \log(T-1)/(T-2)$.

**Remark 1.5.6 (Formalization).** The statement used in Volume 11 and the ramified slope formula are two definitions with the same body, and the proof that they agree is reflexivity ([SlopeLineRamifiedFormula.lean](lean:Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/SlopeLineRamifiedFormula.lean#L47), [FiniteModelOfAdmissibleTransports.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/FiniteModelOfAdmissibleTransports.lean#L1553)). The theorem for a character of finite order takes the trivial stabilizers as a hypothesis, although they follow from the compatible forms; the final theorem supplies them in this way ([SlopeLineRamifiedFormula.lean](lean:Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/SlopeLineRamifiedFormula.lean#L57)). The splitting of the CM extension at the places of $\mathfrak{v}_T$ is proved for every datum of the type used here, so the corollary on split primes needs no further input. The four parts of the proposition were opened as statements; the sketches of their proofs follow the first lines of the formal proofs and do not cover every step.
