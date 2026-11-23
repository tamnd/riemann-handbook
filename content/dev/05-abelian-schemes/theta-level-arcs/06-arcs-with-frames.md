---
title: Arcs with frames
decls:
  - GlobalTheory.T.exists_arc_family_point_with_frames_of_laws
  - GlobalTheory.Ex.arcFam
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Arcs with frames

In this section we prove the arc family theorem. For each arc $a$ over an arc base and each odd $m$ that is a unit in $O'$, there are a finite normal extension $R_1$ of $O'[[X]]$ and a point $y_1$ of the moduli space over $\operatorname{Frac} R_1$ with trait data for $a$, a frame of level $1$ with one section, and a frame of level $m^2$. The proof puts together [the moduli point of an arc](/entry/exists-point/), two results on the behaviour at complete traits, a result on frames of level $1$, and [the frames of level $m^2$](/entry/exists-is-frame-pow-sq/). The theorem is used in [the closed form of the arc family statement](/entry/arc-fam-closed/), and through it in [the fourth clause of the models](/entry/arc-family-fourth-condition-invertible-pushforward/).

### The statement

We keep the notation of the earlier sections: $Y$ is a model of $X_o$ over $V$, $(O', \varpi)$ is an arc base with $O'$ of characteristic $0$, $b : V \to O'$, and $a$ is an arc over $(O', b)$. Trait data and frames are defined in [the previous section](/entry/exists-is-frame-pow-sq/).

**Definition 6.6.1 (Arc family statement).** The *arc family statement* says: for all such $Y$, $(O', \varpi)$, $b$ and $a$, and for every odd $m$ that is a unit in $O'$, there are an integrally closed domain $R_1$, an injective and finite map $g : O'[[X]] \to R_1$ and a point $y_1$ of $X_{o,F}$ over $\operatorname{Frac} R_1$ such that:

1. $(g, y_1)$ has trait data for $a$;
2. there is a frame $(\theta)$ of level $1$ at $j \circ y_1$, with one section;
3. there is a frame of level $m^2$ at $j \circ y_1$.

Lean: `GlobalTheory.LN.ArcFamSt`.

In words, an arc point with trait data is abelian where $X$ is a unit and has the degeneration data of $a$, with period parameter $X$, where $X$ is not a unit. The two frames are what the construction of the models needs to embed the family in a projective space.

### Inputs on traits and frames

We use four results of the Lean development that this chapter does not prove. Each assumes the seven inputs, and in each, $R_1$ is an integrally closed domain, $g : O'[[X]] \to R_1$ is injective and finite, and $y_1$ is a point of $X_{o,F}$ over $\operatorname{Frac} R_1$ that lies over $b$.

**Theorem 6.6.2 (Arc data at bad traits).** If $(g, y_1)$ realises $a$, then the second condition of trait data holds: at each complete trait $W$ through $y_1$ at which $g(X)$ is not a unit, after a finite extension $W'$ of complete traits, the point has the arc data of $a$ with parameter the image of $g(X)$.

Lean: `GlobalTheory.Ex.Trait.hasArcData_at_trait`.

**Theorem 6.6.3 (Good traits).** If $(g, y_1)$ has integral theta points, then the first condition of trait data holds: at each complete trait $W$ through $y_1$ at which $g(X)$ is a unit, the extension $\chi$ maps into the abelian locus.

Lean: `GlobalTheory.Ex.GoodTrait.range_subset_abLocus`.

The idea of the second theorem is that an integral family with a unit in every coset of $n^{j-1}\Lambda$ is the theta point of an abelian scheme over $W$, so the fibre over the closed point is proper.

**Theorem 6.6.4 (A frame of level 1).** If $(g, y_1)$ has trait data for $a$ and integral theta points, then there are an integrally closed domain $R_2$, an injective and finite map $h : R_1 \to R_2$ with a compatible map $h'$ of fraction fields, and a frame of level $1$ with one section at $j \circ y_1 \circ h'$.

Lean: `GlobalTheory.T.exists_single_polarisation_generator_all_traits`.

**Theorem 6.6.5 (Stability under finite extensions).** Let $h : R_1 \to R_2$ be a finite map of domains with a compatible map $h'$ of fraction fields. If $(g, y_1)$ has trait data for $a$, then so does $(h \circ g, y_1 \circ h')$. If $(g, y_1)$ realises $a$, then so does $(h \circ g, y_1 \circ h')$. If $f$ is a frame of level $N$ at $j \circ y_1$, then there is a frame of level $N$ with the same number of sections at $j \circ y_1 \circ h'$.

Lean: `GlobalTheory.Ex.Mono.mono`.

### The theorem

**Theorem 6.6.6 (Arc family).** Assume the seven inputs. Then the arc family statement holds.

Lean: `GlobalTheory.T.exists_arc_family_point_with_frames_of_laws` (also `GlobalTheory.Ex.arcFam`, a second name).

*Proof.* Fix $Y$, $(O', \varpi)$, $b$, $a$ and an odd $m$ that is a unit in $O'$.

*Step 1.* By the theorem on the moduli point of an arc, there are $R_1$, $g$ and $y_1$ such that $R_1$ is integrally closed, $g$ is injective and finite, $y_1$ lies over $b$, and $(g, y_1)$ realises $a$ and has integral theta points.

*Step 2.* The pair $(g, y_1)$ has trait data for $a$. The first condition is the theorem on good traits, applied with the integral theta points. The second condition is the theorem on arc data at bad traits, applied with the realisation.

*Step 3.* By the theorem on a frame of level $1$, applied with the trait data and the integral theta points, there are $R_2$, $h : R_1 \to R_2$ and $h'$ such that $R_2$ is integrally closed, $h$ is injective and finite, and there is a frame $(\theta)$ of level $1$ at $j \circ y_1 \circ h'$. By stability under finite extensions, the pair $(h \circ g, y_1 \circ h')$ has trait data for $a$ and realises $a$. The map $h \circ g$ is injective and finite.

*Step 4.* By the theorem on frames of level $m^2$, applied to $(h \circ g, y_1 \circ h')$ with the trait data, the realisation and the frame $(\theta)$, there are $R_3$, $k : R_2 \to R_3$ and $k'$ such that $R_3$ is integrally closed, $k$ is injective and finite, and there is a frame of level $m^2$ at $j \circ y_1 \circ h' \circ k'$.

*Step 5.* By stability under finite extensions along $k$, the pair $(k \circ h \circ g, y_1 \circ h' \circ k')$ has trait data for $a$, and the frame $(\theta)$ of level $1$ gives a frame $(\theta')$ of level $1$ with one section at $j \circ y_1 \circ h' \circ k'$.

So $R_3$, the injective and finite map $k \circ h \circ g$, and the point $y_1 \circ h' \circ k'$ satisfy the three conditions of the arc family statement. $\square$

**Remark 6.6.7 (Formalization).** The Lean proof is in [ExistsArcFamilyPointWithFramesOfLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsArcFamilyPointWithFramesOfLaws.lean#L20), and the statement form is proved by a `first | exact ...` block in [ExistsArcFamilyPointWithFramesOfLawsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsArcFamilyPointWithFramesOfLawsStatement.lean#L12). The two uses of stability discard different parts: at line 33 the part on frames is dropped, and at line 38 the part on realisation is dropped. The realisation passed to the theorem on frames of level $m^2$ is not used there, so the transport of the realisation in Step 3 serves no purpose in the end. The four inputs of this section are proved elsewhere in the development; the theorem on a frame of level $1$ is proved by `GlobalTheory.Ex.OneGen.main`, and the theorem on good traits uses `T.isProper_of_theta_unit_in_every_coset`. We did not unfold `abLocus`, `Model.HasArcData` or the seven inputs.
