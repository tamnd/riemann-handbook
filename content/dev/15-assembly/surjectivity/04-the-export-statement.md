---
title: The export statement
decls:
  - GlobalTheory.BigOn.Exp.exportSt_of_hypotheses_alt
  - GlobalTheory.T.exportSt_of_discrete_series_cover
  - GlobalTheory.BigOn.exportSt_of_reading_alt
  - GlobalTheory.T.exportSt_of_reciprocity_and_casselman_wallach
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The export statement

This section proves the export statement: at the rich points of a family, at each twisted place $v$ and each level $j$, there is a semilinear map from the coefficient space to the extended space of forms at $v$ that reads the theta base lattice through the idempotent of level $j$. The proof checks thirteen conditions at the twisted places and joins them. It uses six inputs: four published theorems and two statements that come from class field theory. The surjectivity statement of [Section 5.10.7](/entry/onto-x-of-hypotheses-alt-alt/) gives the export statement to the twist bound. The background on [unramified representations](/learn/representations/#unramified-representations) and on the [discrete series](/learn/real-groups/#discrete-series-and-formal-degrees) is in Volume 1.

We first state the inputs.

**Theorem 5.4.1 (Rapid decay of cusp forms).** Let $G$ be the unitary group of a hermitian space over a CM field, with an infinite family of embeddings. Let $\varphi$ be an automorphic function on $G(\mathbb{A})$ that is smooth at the infinite places, of uniform moderate growth, and cuspidal. Then $\varphi$ is of rapid decay on Siegel sets.

Lean: `GlobalTheory.Published.CuspRapidDecay`.

This is a classical result of reduction theory; see Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Chapter I, and Moeglin and Waldspurger, *Spectral Decomposition and Eisenstein Series*, Chapter I.

**Theorem 5.4.2 (Global Artin reciprocity).** For each number field $E$ with an algebraic closure $\Omega$ there is a continuous homomorphism from the ideles of $E$ to the abelianized Galois group of $\Omega / E$ with the properties of the global Artin map.

Lean: `GlobalTheory.Published.GlobalArtinReciprocity` (also `GlobalTheory.Published.RayClassFieldSt`, the existence of ray class fields with an Artin isomorphism).

This is the reciprocity law of global class field theory (Neukirch, *Algebraic Number Theory*, Chapter VI, §§6 and 7). In the proof of Section 10 both statements come from the hypothesis on $\ell$-adic characters of Hecke characters, which contains a global Artin map.

**Theorem 5.4.3 (The discrete series).** Let $p + q \ge 1$ and let $T$ be the group data of $U(p, q)$. There is a map $D$ from the Harish-Chandra parameters $\lambda$ of $U(p, q)$ to discrete series representations such that $D(\lambda)$ has the $K$-types of $\lambda$, and each discrete series representation is unitarily equivalent to some $D(\lambda)$.

Lean: `GlobalTheory.Published.DiscreteSeriesCover`.

This is the classification of the discrete series of Harish-Chandra (*Discrete series for semisimple Lie groups II*, Acta Math. 116, 1966).

**Theorem 5.4.4 (Casselman-Wallach).** Let $\sigma$ be an irreducible unitary representation of $U(n)$ for a sign vector $\varepsilon$ on a Hilbert space $H$, and let $E$ be a smooth Fréchet representation of moderate growth. Each $(\mathfrak{g}, K)$-map from the $K$-finite vectors of $H$ to $E$ extends to a continuous map of the smooth vectors.

Lean: `GlobalTheory.Published.CasselmanWallach`.

This is the canonical globalization theorem of Casselman and of Wallach (*Real Reductive Groups II*, Chapter 11).

The sixth input is the rational series statement. It says that the theta values of the frame pins at the base embedding are rational, for each core datum with its laws, its group, family, models and theta pins, and its ties. It is proved from the hypothesis on $\ell$-adic characters of Hecke characters.

Lean: `GlobalTheory.SerStd.SeriesRatS`.

**Definition 5.4.5 (Export tie).** Let $p$ be a point, $v$ a twisted place and $j$ a level. An *export tie* at $(v, j)$ is a semilinear map $r$ from $L^{n_W(j)}$ to the extended space of forms at $v$ such that $r$ reads the theta base lattice at $v$ through the idempotent operator of level $j$ and the theta tuple. The reading is taken with the group $U = P_0$, the character $\psi_0^{-1}$ and the prime $\ell_v$.

Lean: `GlobalTheory.TwistIndex.ExportTie`.

**Definition 5.4.6 (Export statement).** The *export statement* is the closed property: eventually at the points of $\mathcal{F}$, for each rich point $p$, each twisted place $v$ of $p$ and each level $j$, there is an export tie at $(v, j)$ with the own prime $\ell_v$.

Lean: `GlobalTheory.BigOn.ExportedStatement`.

**Theorem 5.4.7 (The export statement).** Assume rapid decay of cusp forms, global Artin reciprocity, the existence of ray class fields, the classification of the discrete series, the Casselman-Wallach theorem and the rational series statement. Then the export statement holds.

Lean: `GlobalTheory.BigOn.Exp.exportSt_of_hypotheses_alt` (also `GlobalTheory.T.exportSt_of_discrete_series_cover`, `GlobalTheory.BigOn.exportSt_of_reading_alt` and `GlobalTheory.T.exportSt_of_reciprocity_and_casselman_wallach`, second names).

*Proof.* Each condition below has the form: eventually at the points, the condition holds at each twisted place $w$ and each level $j$. Such conditions are closed under finite conjunctions.

1. Five conditions hold with no input. A canonical map exists, and the images of a basis are linearly independent. The canonical map commutes with the projection. The twist is admissible. Each prime that divides a fixed integer of the host lies in the set $S_0$ of the twist. An adapted setup exists.
2. From the admissible twist, global Artin reciprocity gives the twist character, and the recursive side holds.
3. The rationality at the place follows from rapid decay, the two class field statements, the rational series statement and step 1. Then the rational compatibility holds.
4. The base lattice does not change under a change of setup; this uses the ray class fields and the rational series statement. The twisted lattice does not change either; this uses the discrete series and the Casselman-Wallach theorem, and it is their only use.
5. Two inclusions each way hold between the lattices of the canonical map and the base and twisted lattices.

At a point beyond all thresholds, take a twisted place $v$, a level $j$, an export tie candidate and a setup that fits. Step 5 gives the equality of the lattices of the canonical map with the base lattice in this setup. Step 4 moves the equality to the setup of the candidate. This gives the reading, and so the export tie. $\square$

**Remark 5.4.8 (Formalization).** The theorem is in [ExportStOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfPrints.lean#L27). The statement is in [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L33), and the export tie in [LeafTW1OfAllConjugatesGood.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/LeafTW1OfAllConjugatesGood.lean#L365). The same statement has four names in a row: [ExportStOfReadingStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfReadingStatement.lean#L11) calls [ExportStOfReading.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfReading.lean#L11), which calls [ExportStOfPrintsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfPrintsStatement.lean#L11), which calls the theorem. Two of the wrappers set `maxHeartbeats` to 1000000 for a one-line call. The words "prints", "reading", "discrete series cover" and "reciprocity and Casselman-Wallach" name files or single inputs, not the statement. ExportSt.lean has empty sections at lines 15 to 21 and 49 to 52. We read the five steps from the names of the thirteen conditions and have not opened the lemmas, the reading relation or the extended space of forms. The statement of the Casselman-Wallach input above is our reading of a long Lean type; we have not checked it against the published theorem. The rational series statement is not a published result: it is proved in this volume, and it is placed with the inputs only because the export theorem takes it as a hypothesis. In Section 10 the export statement is not used by the final step, which proves its own copies of the page, geometric and rank statements.
