---
title: Rationality, finiteness and the second nonvanishing
decls:
  - GlobalTheory.HeightCounting.RatSide.sRat_of_isotInternal_alt_alt
  - GlobalTheory.HeightCounting.RatSide.sRat_of_isotInternal_inputs
  - GlobalTheory.HeightCounting.Up.secondNo_of_sMt_sRat_sCusp_sFinl
  - GlobalTheory.HeightCounting.Up.sFino_and_secondNo_of_rat_cusp_finl
  - GlobalTheory.T.sFino_and_secondNo_of_sFinl'
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rationality, finiteness and the second nonvanishing

This section proves two things. The first is the rationality statement: at every stage, a same Galois level datum gives a rationality input, when the spaces of the stage are internal direct sums of their isotypic parts. It is part of item 2 of [the stage statements](/entry/all-stages-of-specializations-alt/) of Section 6. The second is the finiteness and nonvanishing theorem, which gives at a constant $c_{\mathrm{Dep}}$ the spectral finiteness statement and the second nonvanishing statement. Step 3 of [the Theorem on the origin extension](/entry/exists-base-lattice-of-prime-alt/) of Section 1 uses it, and the second nonvanishing statement is the pass hypothesis of the pair theorem there. Its proof assembles the stage statements: it builds a strict henselian acyclic level at a stage, enlarges the base, rebuilds the levels on the enlarged base, and moves the third level datum back with the moving statement of Section 11.

We keep the notation of Sections 6, 9, 11 and 12. Let $h_L$ be a recursion datum and $c_{\mathrm{Dep}} \in \mathbb{R}$. Write $N_\ell$ for the extension with list for $h_L$ and $c_{\mathrm{Dep}}$, $N_0$ for the origin extension and $N_g$ for the geometric extension of Section 1. For an $S$-extension $S$ and a geometric predicate $\Gamma$, write $p(N, S, \Gamma)$ for the parameter set with position $\mathrm{RX}$, extension $N$, $S$-extension $S$ and geometry $\Gamma$, and $s(N, S, \Gamma)$ for its scale.

**Definition 6.13.1 (Isotypic decomposition).** A datum $D$ with $m$ rows is *isotypic internal* if for each $j$ with $1 \leq j \leq m$, the space of $D$ at $j$ is the internal direct sum of its isotypic parts under the Hecke algebra: every vector is a unique finite sum of vectors in the isotypic parts.

**Definition 6.13.2 (Rationality input).** Let $x$ be a stage with real datum $Y$ and character group $G$. A *rationality input* for $(Y, G)$ consists of a finite set $S_b$ of places, a representation $\rho$ and a character $\chi$ of $G$, weights, a finite dimensional space with a finitely generated lattice, Hecke operators $h$ with eigenvalues in $L_0$ outside $S_b$, a nonzero character $\theta$, and the condition that the eigenspaces of $h$ for $\theta$ span the space and that the eigenvalues are integral. The *rationality statement* for $h_L$ says that at all stages $x$, each same Galois level datum over $x$ gives a rationality input for $x$.

**Definition 6.13.3 (Statements at all stages).** Let $h_L$ be a recursion datum.

1. The *matrix input statement* says that at all stages $x$ of a datum $P$ of a column datum $w$, there is a matrix input for the real datum of $x$, the character frame of $x$, the character $\xi$ of $w$ and the place map of $P$.
2. The *cusp statement* says that at all stages, each same Galois level datum satisfies the row cusp condition of Section 6.
3. The *finiteness list statement* at $c_{\mathrm{Dep}}$ says that at all stages $x$ of a datum $P$, for each strict henselian acyclic level datum $l$ over $x$ and each $S$ and $\Gamma$, if the list condition for $c_{\mathrm{Dep}}$ holds at $x$, then there are a stage $Z$ and a level three object $v$ at $s(N_\ell, S, \Gamma)$ and $Z$ whose weights are those of $P$ and whose norm choice is kept by the character choice of $l$.
4. The *spectral finiteness statement* at $c_{\mathrm{Dep}}$ is the same with $N_0$ in place of $N_\ell$ and with the hypothesis that the list condition holds at $x$ and $P$ is unlocalized saturated.
5. The *second nonvanishing statement* at $c_{\mathrm{Dep}}$ says that for each $S$ and $\Gamma$, the pass condition holds for $\mathrm{KP}_x$ and the built cores of $s(N_0, S, \Gamma)$ with target the property: there is a column datum $w$ with the start condition and $\mathrm{Has}_3(s(N_g, S, \Gamma))$ at $w$.

We also use three conditions that are not statements from the literature. The *weight case condition* is the subject of Section 15. The *data extension condition* says that, along $\mathrm{Step}_w$ from the pinned condition, fine data with the lower unitary case condition over a base extend along enlargements of the base. The *continuity condition* says that for each datum, each frame, each Weil-Deligne tie $T$ and each Weil-Deligne side at $T$, the Galois representations of the side are continuous maps to $\mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$.

**Theorem 6.13.4 (Rationality statement).** Assume $\mathcal{P}$ and $\mathcal{S}$, and assume that at all stages $x$ the datum $D_x$ is isotypic internal. Then the rationality statement holds for every recursion datum $h_L$.

Lean: `GlobalTheory.HeightCounting.RatSide.sRat_of_isotInternal_alt_alt` (also `GlobalTheory.HeightCounting.RatSide.sRat_of_isotInternal_inputs`, a form with one more hypothesis).

*Proof.* Five statements hold at all stages together. By $\mathcal{P}$, the forms of the stage have a lattice over the coefficient ring, and theta data exist at the stage. By $\mathcal{P}$ and $\mathcal{S}$ (the decay of the forms, the Hecke traces and the Hecke readings), the Hecke operators act on the forms with eigenvalues in $L_0$ outside a finite set; with the integrality of Hecke operators in $\mathcal{S}$, the eigenvalues are integral and stable under the level. Since $D_x$ is isotypic internal, the eigenspaces span the space. Fix a stage $x$ and a same Galois level datum. The stabilizer of $\rho$ lies in the character group of $L_0$, so $\rho$ and $\chi$ are defined over $L_0$. The finite set $S_b$, $\rho$, $\chi$, the weights, the lattice, the Hecke operators, the eigenvalues, the character $\theta$ with $\theta \neq 0$, the span and the integrality give the rationality input. $\square$

**Theorem 6.13.5 (Second nonvanishing).** Assume the discrete series cover, the Casselman-Wallach theorem, the theory of Harish-Chandra modules and the existence of discrete series (the first three as in Section 12), $\mathcal{P}$, $\mathcal{S}$, the data extension condition, the weight case condition and the continuity condition. Let $h_L$ be a recursion datum with the matrix input statement, the rationality statement and the cusp statement, and let $c_{\mathrm{Dep}} \in \mathbb{R}$ with the finiteness list statement at $c_{\mathrm{Dep}}$. Then the second nonvanishing statement holds at $c_{\mathrm{Dep}}$.

Lean: `GlobalTheory.HeightCounting.Up.secondNo_of_sMt_sRat_sCusp_sFinl`.

*Proof.* Fix $S$ and $\Gamma$. The data extension condition and Green's classification in $\mathcal{P}$ give twisted places at every extension. Nine statements hold together eventually:

1. the construction starting choices of fine adelic data, from the Weil representation of a unitary pair (a proved theorem), the existence of discrete series, parts of $\mathcal{P}$ and the weight case condition;
2. the existence of bare stages, from the existence of discrete series;
3. the same Galois level statement, item 1 of the stage statements, from $\mathcal{P}$ and the continuity condition;
4. the matrix input statement;
5. the rationality statement;
6. the cusp statement;
7. [the moving statement](/entry/multiplicity-bound-of-local-components-alt/) of Section 11;
8. [the strict henselian acyclic levels](/entry/stage-cexists-of-harish-chandra-ser-n/) of Section 12;
9. the spectral finiteness statement, which follows from the finiteness list statement because the list condition and the saturation of $P$ give the origin datum $(P, x, l)$.

Now let $K$ be a context and $B$, $f$, $T$ data with $\mathrm{KP}_x(B, f)$ and a built core $c$ of $s(N_0, S, \Gamma)$. The pass condition reduces us to such a core. The core lies in the slot, so there are a column datum $w$, a stage $Z$ and $c$ in position, and $w$ satisfies the start condition. The origin datum of the built core gives a datum $P$, a stage $x$ and a strict henselian acyclic level $l$ with the list condition and the saturation of $P$.

Choose a seed $\sigma$ that avoids the places of two finite sets $A$ and $A_1$ of bad places. The lift of twisted cohomology classes gives an enlargement $B \to B'$ with the same primes, with frame $f'$ and twist datum $T'$, that avoids $A$ and contains the places of $S_2$. There is a column datum $w'$ over $B'$ that matches $w$, with the start condition. Statement 1 gives a datum $P'$ of $w'$ that extends $P$. Statement 2 gives a bare stage $x_0$ of $P'$, and statement 3 gives a stage $x_1$ with a same Galois level datum and the same Galois data. Statements 4 to 6 give an intermediate level datum at $x_1$. Statement 7, applied to $x$, $P'$ and $x_1$, gives a stage $y$ of $P'$ with a third level datum, carried from $D_x$, with the list condition. Statement 8 extends it to a strict henselian acyclic level datum, and statement 9 gives a level three object at $s(N_0, S, \Gamma)$. Since the Galois data are carried, the good orientation condition holds, and we get $\mathrm{Has}_3(s(N_g, S, \Gamma))$ at $w'$. $\square$

**Theorem 6.13.6 (Finiteness and nonvanishing).** Under the hypotheses of the theorem on the second nonvanishing, the spectral finiteness statement and the second nonvanishing statement hold at $c_{\mathrm{Dep}}$.

Lean: `GlobalTheory.HeightCounting.Up.sFino_and_secondNo_of_rat_cusp_finl` (also `GlobalTheory.T.sFino_and_secondNo_of_sFinl'`, a second name).

*Proof.* The spectral finiteness statement follows from the finiteness list statement, as in statement 9 above. The second part is the theorem on the second nonvanishing. $\square$

**Remark 6.13.7 (Formalization).** The theorems are at [SRatOfIsotInternal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SRatOfIsotInternal.lean#L28) (the second form at line 63) and [FiniteLevelAndSecond.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FiniteLevelAndSecond.lean#L72) (lines 116 and 125). The form `sRat_of_isotInternal_inputs` is `fun _ => …`, so its hypothesis `DiscreteSeriesUpqUnique` is not used. In statement 1 of the second nonvanishing the Weil representation of a unitary pair enters as the proved theorem `GlobalTheory.weilRepresentationUnitaryPair`, not as a hypothesis. The step from the finiteness list statement to spectral finiteness is `sFino_of_alt` ([ExistsSeed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsSeed.lean#L21)), which copies the level three object and adds the origin datum. The isotypic condition is `IsotInternal` (DataRows.lean, line 241), the matrix input statement is `SMt`, the cusp statement is `CuspStatement'`, the finiteness list statement is `FinitenessListStatement` and the data extension condition is `DatExt`. The continuity condition is `PhtCmp`. We did not unfold `DatExt`, `InRat`, `InMt`, `Pass`, `Has3` or the lift of twisted cohomology classes, so the definitions above give their roles, and the proof of the second nonvanishing follows the statements of the lemmas it calls.
