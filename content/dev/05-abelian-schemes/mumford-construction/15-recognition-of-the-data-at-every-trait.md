---
title: Recognition of the data at every trait
decls:
  - GlobalTheory.Mum.Recog.recognition_core
  - GlobalTheory.T.galois_equivariant_torsion_values_ultrametric
  - GlobalTheory.Mum.Recognition.pullDeg_induces
  - GlobalTheory.T.recognition_degData_labels_at_every_trait
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Recognition of the data at every trait

This section proves that labels which are correct at one complete trait are correct at every complete trait. More precisely, let $D$ be degeneration data over a base $R$, and let $A$ be a polarised abelian variety over $K$ with labels of its torsion points by torsion classes of $D$. If the labels match a uniformisation by a pullback of $D$ at one trait, and they are Galois equivariant, then at every complete trait $W$ over $R$, every uniformisation whose generic fibre is a fibre of $A$ comes from a pullback of $D$, and it matches the labels. The trait condition of a [labelled cover](/entry/has-fin-of-lab-cover/) asks for exactly this, and [the theorem on labelled covers from uniformised covers](/entry/lab-cover/) uses the result to check it. The main tool is the recognition theorem for degeneration data at a trait: data are determined by their torsion values and their theta constants.

Throughout, $R$ is a base with fraction field $K$, and $\bar K$ is an algebraic closure of $K$. We use the torsion classes $Q_k(D)(F)$ of [the section on torsion of tensor data](/entry/tate-tens/) and the phrases "$p'$ is the image of $p$" and "$U'$ carries $p'$ to $x'$" as in [the section on labelled covers](/entry/has-fin-of-lab-cover/).

### Labels and traits

Let $D$ be degeneration data over $R$ and $A$ a polarised abelian variety over $K$. *Labels* of $D$ in $A$ are maps $\ell_k : Q_k(D)(\bar K) \to A(\bar K)$, one for each $k \geq 0$.

**Definition 4.15.1 (Fibre of a polarised abelian variety).** Let $\varphi : R \to W$ be a ring map of domains, $A$ a polarised abelian variety over $K$ and $A'$ one over $\operatorname{Frac} W$. A morphism $a : A' \to A$ makes $A'$ a *fibre* of $A$ over $\varphi$ if there is a field map $g : K \to \operatorname{Frac} W$ that extends $\varphi$, such that $a$ makes $A'$ the group pullback of $A$ along $\operatorname{Spec} g$, and there is a generating isomorphism $L_{A'} \cong a^* L_A$.

Lean: `GlobalTheory.Mum.IsFib`.

**Definition 4.15.2 (Labels induce a uniformisation).** Let $\varphi : R \to W$ be a ring map of local domains, $D'$ degeneration data over $W$ with a structure of pullback of $D$ along $\varphi$, $U'$ a uniformisation of $(A', G')$ by $D'$, and $a : A' \to A$ a morphism. The labels $(\ell_k)$ *induce* $U'$ at level $k$ if the following holds. Let $F$ be an algebraically closed field over $\operatorname{Frac} W$ and over $K$, such that the two maps $R \to F$ agree through $\varphi$, and let $e : \bar K \to F$ be a $K$-embedding. Let $p \in Q_k(D)(\bar K)$, let $p_1 \in Q_k(D)(F)$ be its image under $e$, let $p' \in Q_k(D')(F)$ be the image of $p_1$, and let $x' \in A'(F)$ with $a(x') = e(\ell_k(p))$. Then $U'$ carries $p'$ to $x'$.

Lean: `GlobalTheory.Mum.Induces`.

**Definition 4.15.3 (Labels correct at one trait).** The labels $(\ell_k)$ are *correct at one trait* if there are a complete trait $W$, an injective local map $\varphi : R \to W$, a commutative semi-abelian scheme $G'$ over $W$, data $D'$ over $W$ with a structure of pullback of $D$ along $\varphi$, a uniformisation $U'$ of $(A', G')$ by $D'$, a morphism $a : A' \to A$ that makes $A'$ a fibre of $A$ over $\varphi$, and a $K$-embedding $e : \bar K \to \overline{\operatorname{Frac} W}$ that agrees with $\varphi$ on $R$, such that the condition of the previous definition holds with $F = \overline{\operatorname{Frac} W}$, this $e$, and every $k \geq 1$.

Lean: `GlobalTheory.Mum.OneTrait`.

**Definition 4.15.4 (Galois equivariant labels).** Let $n \geq 1$. The labels are *Galois equivariant at the powers of $n$* if $\ell_{n^j}(\sigma p) = \sigma(\ell_{n^j}(p))$ for every $K$-automorphism $\sigma$ of $\bar K$, every $j \geq 0$ and every $p \in Q_{n^j}(D)(\bar K)$.

Lean: `GlobalTheory.Mum.GalEqN`.

In the proof we also use good labellings. Over a field $F$, a family of maps $f_k : Q_k(D)(F) \to A(F)$ is a *good labelling* if each $f_k$ maps onto the $k$-torsion of $A(F)$, identifies exactly the equivalent classes, and is compatible with addition, with the Weil pairing and with the maps between levels. A uniformisation of $(A, G)$ by $D$ over a complete trait gives a good labelling $f$ over every algebraically closed $F$, with $U$ carrying $p$ to $x$ if and only if $x = f_k(p)$.

### Theta families

The first theorem has one more hypothesis, on theta values. Let $k$ be odd and a unit. A family of values $(v_i)$ over a base $T$ is a *theta family of level $k$* for a family of points $(x_i)$ of $A$ if, locally on $T$, there are a generating section $\theta$ of $L_A$, its pullback $s$ along multiplication by $k$ read as a section of $L_A^{k^2}$, symmetric lifts $U_i$ of the translations by $x_i$ to the theta group of $L_A^{k^2}$, and a unit $u$, such that $v_i = u \cdot (U_i s)(0)$ for all $i$. So up to one common unit, the $v_i$ are the values of the translates of $[k]^* \theta$ at the zero section.

Let $n$ be an odd prime that is a unit in $R$. We say that $D$, $A$ and $(\ell_k)$ satisfy *condition* $(\Theta)$ if the following holds for every $j \geq 0$ and every map $v : Q_{n^{2j}}(D)(\bar K) \to \bar K$. Suppose that for every complete, ultrametric, algebraically closed field $C$ over $K$ in which $R$ lies in the unit ball and $\mathfrak{m}$ in the open unit ball, every $K$-embedding $e : \bar K \to C$, every system $N$ of numerical degeneration values over $C$ that realises $D$, and every choice of images $p_1(i) \in Q_{n^{2j}}(D)(C)$ and torsion indices $q(i)$ of $N$ matching them, there is a unit $s \in C^\times$ with $e(v(i)) = s \cdot t_{n^j}(q(i))$ for all $i$. Here $t_{n^j}$ is the theta series of $N$ at level $n^j$. Then $v$ is a theta family of level $n^j$ for the points $\ell_{n^{2j}}(i)$.

So condition $(\Theta)$ says: values that look like the theta constants of $D$ at every ultrametric place are theta values for the labelled points.

### Recognition at one embedding

**Theorem 4.15.5 (Recognition at one embedding).** Let $R$ be a base, $D$ degeneration data over $R$, $A$ a polarised abelian variety over $K$ and $(\ell_k)$ labels of $D$ in $A$. Let $n$ be an odd prime that is a unit in $R$. Assume that the labels are correct at one trait, that they are Galois equivariant at the powers of $n$, and that condition $(\Theta)$ holds. Let $W$ be a complete trait, $\varphi : R \to W$ an injective local map, $G'$ a commutative semi-abelian scheme over $W$, $D'$ data over $W$, $U'$ a uniformisation of $(A', G')$ by $D'$, and $a : A' \to A$ a morphism that makes $A'$ a fibre of $A$ over $\varphi$. Then there are a structure of pullback of $D$ along $\varphi$ on $D'$, an algebraically closed field $C$ over $\operatorname{Frac} W$ and over $K$ in which the two maps $R \to C$ agree through $\varphi$, and a $K$-embedding $e : \bar K \to C$, such that the condition of the definition of induced uniformisations holds with $F = C$, this $e$ and every level $n^j$, $j \geq 0$.

Lean: `GlobalTheory.Mum.Recog.recognition_core` (also `GlobalTheory.T.galois_equivariant_torsion_values_ultrametric`, a second name).

*Proof.* *Step 1: the labels are good.* Let $(W_0, \varphi_0, U_0, a_0, e_0)$ be the trait at which the labels are correct. The uniformisation $U_0$ gives a good labelling $g_0$ over $\overline{\operatorname{Frac} W_0}$. By correctness, $g_0$ agrees with the labels moved along $e_0$ and $a_0$. A good labelling moved back along an embedding and a fibre map is good, so $(\ell_k)$ is a good labelling over $\bar K$.

*Step 2: the field.* Let $D_W$ be a pullback of $D$ along $\varphi$; it exists since $\varphi$ is injective and local. Let $C$ be a complete, ultrametric, algebraically closed field over $\operatorname{Frac} W$ in which $W$ lies in the unit ball and its maximal ideal in the open unit ball. Through $\varphi$ it is a field over $K$, and we choose a $K$-embedding $e : \bar K \to C$.

*Step 3: two good labellings over $C$.* The fibre map $a$ and $e$ give a map $\varepsilon$ from $A(\bar K)$ to $A'(C)$. Moving the labels along $e$ and $\varepsilon$ gives maps $f^W_k$ on $Q_k(D_W)(C)$, and they form a good labelling by Step 1. The uniformisation $U'$ gives a second good labelling $f'$ on $Q_k(D')(C)$.

*Step 4: numerical values.* Since $n$ is a unit in $W$, $|n| = 1$ in $C$. Both $D_W$ and $D'$ have integral numerical degeneration values $N$ and $N'$ over $C$. The torsion values of $N$ are $n$-divisible, and some theta constant of $N$ at level $n$ is non-zero.

*Step 5: Galois equivariance.* The equivariance of the labels over $K$ moves to equivariance of $f^W$ under the automorphisms of $C$ over $\operatorname{Frac} W$, by restriction to the normal closure. The labelling $f'$ is equivariant since it comes from a uniformisation over $W$. Together: if $f^W(p) = f'(p')$ at level $n^2$, then $f^W(\sigma p) = f'(\sigma p')$ for every $\sigma$.

*Step 6: proportional theta constants.* For each $j$ there is a unit $c \in C^\times$ such that $t'_{n^j}(q') = c \cdot t_{n^j}(q)$ whenever the torsion indices $q$ of $N$ and $q'$ of $N'$ belong to classes $p$, $p'$ with $f^W(p) = f'(p')$ at level $n^{2j}$. The theta series of $D$ are algebraic over the fraction field, so they come from a map $v$ as in condition $(\Theta)$; by $(\Theta)$ they are theta values for the labelled points. The theta constants of $D'$ are theta values for the same points of $A'$, through $U'$. Two theta families for the same points differ by one unit, which gives $c$.

*Step 7: recognition.* The recognition theorem for degeneration data at a trait now applies to $D_W$ and $D'$ over $W$ with the good labellings $f^W$ and $f'$. It gives a structure of pullback of $D_W$ along the identity of $W$ on $D'$, under which $f^W$ and $f'$ agree at every level $n^j$.

*Step 8: conclusion.* Composing with the pullback structure of $D_W$ over $D$ gives a structure of pullback of $D$ along $\varphi$ on $D'$. Let $p$, $p_1$, $p'$ and $x'$ be as in the definition, with $F = C$. By Step 3, $\varepsilon(\ell(p))$ is $f^W$ of the image of $p_1$, which is $f'(p')$ by Step 7. A point of $A'(C)$ over $e(\ell(p))$ is unique since $a$ is a group pullback, so $x' = f'(p')$, and $U'$ carries $p'$ to $x'$. $\square$

### Recognition at every trait

**Theorem 4.15.6 (Recognition at every trait).** Let $R$ be a base, $D$ degeneration data over $R$, $A$ a polarised abelian variety over $K$ and $(\ell_k)$ labels of $D$ in $A$. Let $n$ be an odd prime that is a unit in $R$. Assume that the labels are correct at one trait and Galois equivariant at the powers of $n$. Let $W$ be a complete trait, $\varphi : R \to W$ an injective local map, $G'$ a commutative semi-abelian scheme over $W$, $D'$ data over $W$, $U'$ a uniformisation of $(A', G')$ by $D'$, and $a : A' \to A$ a morphism that makes $A'$ a fibre of $A$ over $\varphi$. Then there is a structure of pullback of $D$ along $\varphi$ on $D'$ such that the labels induce $U'$ at level $n^j$ for every $j \geq 0$.

Lean: `GlobalTheory.Mum.Recognition.pullDeg_induces` (also `GlobalTheory.T.recognition_degData_labels_at_every_trait`, a second name).

*Proof.* *Step 1: condition $(\Theta)$.* By an input on theta series, condition $(\Theta)$ holds under the two hypotheses on the labels. Its idea is that the theta series of $D$ are algebraic, and at the trait where the labels are correct they are theta values of the uniformised abelian variety.

*Step 2: one embedding.* The theorem on recognition at one embedding gives a structure of pullback of $D$ along $\varphi$ on $D'$, a field $C$ and an embedding $e : \bar K \to C$ at which the labels induce $U'$ at every level $n^j$.

*Step 3: all embeddings.* Fix $j$. By an input on Galois equivariance, if the labels induce $U'$ at level $n^j$ at one algebraically closed field and one embedding, and they are Galois equivariant at the powers of $n$, then they induce $U'$ at level $n^j$. Its idea is that two embeddings of $\bar K$ into algebraically closed fields over $\operatorname{Frac} W$ differ by an element of the Galois group of $K$, up to an extension of fields, and the uniformisation and the classes move along the same element. $\square$

The hypothesis that $n$ is an odd prime that is a unit enters only through the recognition theorem: the theta group at level $n^j$ needs $n$ odd and invertible, and the torsion of $D$ at the powers of $n$ is étale.

**Remark 4.15.7 (Formalization).** The second names are wrappers ([GaloisEquivariantTorsionValuesUltrametricStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GaloisEquivariantTorsionValuesUltrametricStatement.lean#L12) and [RecognitionDegDataLabelsAtEveryTraitStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RecognitionDegDataLabelsAtEveryTraitStatement.lean#L12)). Theta families are `IsThetaPt`, numerical degeneration values are `GlobalTheory.Ex.NumD` with `GlobalTheory.Ex.NumOf`, and good labellings are `GoodLab`; we did not unfold these definitions beyond the sketch above. In the proof of recognition at one embedding ([GaloisEquivariantTorsionValuesUltrametric.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GaloisEquivariantTorsionValuesUltrametric.lean#L21)), Step 1 uses `exists_goodLab` and `goodLab_move`; Step 2 uses `GlobalTheory.MumPull.exists_pull` and `GlobalTheory.T.exists_complete_isAlgClosed_cExt'`; Step 3 uses `exists_ptHom`; Step 5 uses `UT.Cl.galois_holds`; Step 6 uses `GlobalTheory.T.degenerationThetaSeries_algebraic_over_fractionField`, `OneTraitTheta.exists_values_iso`, `theta_constants_eq_degeneration_series` and `RelabelCoords.series_iso`; Step 7 is `rec_trait` ([TorsionTowerRecognition.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsionTowerRecognition.lean#L213)); and Step 8 uses `LabTrans.exists_comp`. Outputs of inputs are discarded at lines 41, 58, 71, 72 and 81. In the second theorem ([RecognitionDegDataLabelsAtEveryTrait.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RecognitionDegDataLabelsAtEveryTrait.lean#L19)), Steps 1 and 3 are `GlobalTheory.T.isThetaPoint_of_algebraic_series_one_trait` and `GlobalTheory.T.labels_induced_all_embeddings_of_galois`. We did not open the proofs of these inputs, and the reasons given for them are sketches. The conclusion of both theorems is strong: any data $D'$ that uniformise a fibre of $A$ at any trait are shown to be a pullback of $D$; this rests on the recognition theorem.
