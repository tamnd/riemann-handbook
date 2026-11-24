---
title: Chern number relations for lattice families
decls:
  - GlobalTheory.T.arithmetic_relations_statement_holds
  - GlobalTheory.CompanionTheory.Ar.Num.TopRel.relations
  - GlobalTheory.T.lattice_family_ckRelations
  - GlobalTheory.CompanionTheory.Ar.Num.CkTop.ckRelations_of_model
  - GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage1
  - GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage1b
  - GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage2
  - GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage3
  - GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage4
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chern number relations for lattice families

This section proves linear relations between the Chern numbers of the bundles of a lattice family on a model over a discrete valuation ring. The relations are twisted by a permutation $\varphi$ of the labels and by powers of a prime $p$. They are used in [the Hodge lattice flag bound from lattice families](/entry/model-on-hodge-of-family-pos/). The proof is a chain of refinements of the model. At each stage we pass to a finer model on which the family has one more good property, and we show that the relations descend from the finer model to the original one. The last stage is [the eigenspace splitting modulo $p$](/entry/stage5/), which the later sections of the chapter prove. For the geometric background see the [semi-abelian degenerations of Volume 1](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).

### Lattice families

Let $O$ be a discrete valuation ring of characteristic $0$ with a uniformizer $\varpi$, and let $\Omega$ be a field over $O$. A model is given by a finite family of coordinates $x$ in $\Omega$, grouped by a finite set $K$ of charts. We assume that $x$ gives a model of relative dimension $d$ over $O$, and that its function field is all of $\Omega$. The charts are the open sets where a chart monomial in $x$ is nonzero; each has a chart ring in $\Omega$.

Let $Sg$ be a finite set of labels, with ranks $r, s : Sg \to \mathbb{N}$. Let $F$ be a finite set with elements $0$ and $1$, let $p$ be a prime, $w \in O$, $\chi_\tau : F \to O$ for $\tau \in Sg$, and let $\varphi$ be a permutation of $Sg$.

**Definition 5.5.1 (Lattice family).** A lattice family is a family $D$ of lattice data, one for each chart, with these properties. The integer $p$ is nonzero and not a unit in $O$, and $w^{p-1} = u p$ for a unit $u$. In $F$ we have $0 \neq 1$, and $\chi_\tau(0) = 0$, $\chi_\tau(1) = 1$ for each $\tau$. On each chart the lattices of $D$ satisfy a base condition and a test condition, and the data are compatible between the charts.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.IsLatticeFamily`.

We do not unfold the base and test conditions. Bundles $\mathrm{Lie}_\tau$, $W_\tau$ of rank $r_\tau$ and $\mathrm{Om}_\tau$, $\mathrm{Om}^{\mathrm{HT}}_\tau$ of rank $s_\tau$ on the model belong to $D$ if on each chart their lattices are those of $D$.

**Definition 5.5.2 (Chern number relations).** Let $\mathrm{Lie}$, $W$, $\mathrm{Om}$ and $\mathrm{Om}^{\mathrm{HT}}$ be bundles on the model. They satisfy the Chern number relations if for each $k$ with $1 \le k \le d + 1$, each $q$, each family $L$ of $q$ divisors with integer coefficients on the charts, and each homogeneous $Q \in \mathbb{Z}[y_1, \dots, y_q]$ of degree $d + 1 - k$, there is $h : Sg \to \mathbb{R}$ with
$$c_\tau = h(\tau) - \frac{k \, \nu_\tau}{p - 1}, \qquad p^k h(\tau) = h(\varphi \tau) + k \, \nu_{\varphi \tau}$$
for all $\tau$. Here $c_\tau$ is the sum of the Chern numbers $c_k(\mathrm{Lie}_\tau, W_\tau; L, Q)$ and $c_k(\mathrm{Om}_\tau, \mathrm{Om}^{\mathrm{HT}}_\tau; L, Q)$, and $\nu_\tau$ is the root number of $\mathrm{Lie}_\tau$ for the power sum of degree $k - 1$, the divisors $L$, the polynomial $Q$ and $p$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CkRelations`.

The Chern number $c_k$ of a pair of bundles is defined by a choice of flag model, and it is $0$ when no flag model exists. We do not unfold it, nor the root number.

### The chain of refinements

In each stage below, $O$, $\Omega$, $x$, $d$, $p$, $w$, $\chi$, $\varphi$ and $D$ are as above, $D$ is a lattice family, and the conclusion is that every choice of bundles that belong to $D$ satisfies the Chern number relations. The conditions $\mathrm{Good}_1$ and $\mathrm{Good}_2$ are properties of the lattice data on each chart that we do not unfold. The annihilator condition says that on each chart and for each $\tau$, $w$ times the standard lattice lies in the lattice $\mathrm{af}_\tau$ of $D$. The line condition says that for each $\tau$ and $i$ the $i$-th distinguished lattice of $D$ is a line bundle on the model.

A refinement of $x$ is a model given by the joined coordinates of $x$ and a second family $z$. The descent lemma of the development says this: if every choice of bundles that belong to the pull back of $D$ to a refinement satisfies the relations, then so does every choice of bundles on $x$ that belong to $D$. A second lemma says that the pull back of $D$ is again a lattice family, and that it transports $\mathrm{Good}_1$, the annihilator condition, $\mathrm{Good}_2$ and the line condition to the refinement.

**Lemma 5.5.3 (Stage 4).** If $D$ satisfies $\mathrm{Good}_1$, the annihilator condition, $\mathrm{Good}_2$ and the line condition, then the relations hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage4`.

*Proof.* There is a refinement of $x$ whose chart rings are integrally closed in $\Omega$. The pull back of $D$ satisfies $\mathrm{Good}_1$, $\mathrm{Good}_2$ and the line condition. By [stage 5](/entry/stage5/) the relations hold on the refinement. By descent they hold on $x$. $\square$

**Lemma 5.5.4 (Stage 3).** If $D$ satisfies $\mathrm{Good}_1$, the annihilator condition and $\mathrm{Good}_2$, then the relations hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage3`.

*Proof.* There is a refinement of $x$ on which the pull back of $D$ satisfies the line condition. The pull back also satisfies $\mathrm{Good}_1$, the annihilator condition and $\mathrm{Good}_2$. By stage 4 the relations hold on the refinement, and by descent they hold on $x$. $\square$

**Lemma 5.5.5 (Stage 2).** If $D$ satisfies $\mathrm{Good}_1$ and the annihilator condition, then the relations hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage2`.

*Proof.* There is a refinement of $x$ on which the pull back of $D$ satisfies $\mathrm{Good}_2$. The pull back also satisfies $\mathrm{Good}_1$ and the annihilator condition. By stage 3 the relations hold on the refinement, and by descent they hold on $x$. $\square$

**Lemma 5.5.6 (Stage 1b).** If $D$ satisfies $\mathrm{Good}_1$ and the chart rings of $x$ are integrally closed in $\Omega$, then the relations hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage1b`.

*Proof.* On each chart the chart ring is noetherian with fraction field $\Omega$, and it is integrally closed. A lemma of the development on Hodge annihilators then gives the annihilator condition for $D$ on the same model. The claim follows from stage 2. $\square$

**Lemma 5.5.7 (Stage 1).** If $D$ satisfies $\mathrm{Good}_1$, then the relations hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage1`.

*Proof.* There is a refinement of $x$ whose chart rings are integrally closed in $\Omega$. The pull back of $D$ satisfies $\mathrm{Good}_1$. By stage 1b the relations hold on the refinement, and by descent they hold on $x$. $\square$

**Theorem 5.5.8 (Chern number relations).** Let $O$ be a discrete valuation ring of characteristic $0$, and let $x$ be a model of relative dimension $d$ over $O$ with function field $\Omega$. Let $D$ be a lattice family on $x$. Then every choice of bundles $\mathrm{Lie}$, $W$, $\mathrm{Om}$ and $\mathrm{Om}^{\mathrm{HT}}$ that belong to $D$ satisfies the Chern number relations.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CkTop.ckRelations_of_model` (also `GlobalTheory.T.lattice_family_ckRelations`, a second name).

*Proof.* There is a refinement of $x$ on which the pull back of $D$ satisfies $\mathrm{Good}_1$, and the pull back is a lattice family. By stage 1 the relations hold on the refinement, and by descent they hold on $x$. $\square$

### Relations for flag pairs

The step that uses these relations states them for local pairs: flag models of the bundles at a point of the special fibre, with Chern numbers $\operatorname{ck}$ and root numbers $\operatorname{la}$ at the ideal $P$ of the point.

**Definition 5.5.9 (Relations for local pairs).** Let $\mathrm{lie}_\tau$ and $\mathrm{om}_\tau$ be local pairs of ranks $r_\tau$ and $s_\tau$. They satisfy the relations if for each $k \ge 1$ and each list $Q$ of divisors with $|Q| + k = d + 1$ there is $h : Sg \to \mathbb{R}$ with
$$\begin{aligned} \operatorname{ck}(\mathrm{lie}_\tau) + \operatorname{ck}(\mathrm{om}_\tau) &= h(\tau) - \frac{\operatorname{la}(\mathrm{lie}_\tau)}{p - 1}, \\ p^k h(\tau) &= h(\varphi \tau) + \operatorname{la}(\mathrm{lie}_{\varphi \tau}) \end{aligned}$$
for all $\tau$, where $\operatorname{ck}$ and $\operatorname{la}$ are taken at $P$, $k$ and $Q$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.Relations`.

**Theorem 5.5.10 (Relations for flag pairs).** Let $O$, $\varpi$, $x$, $d$, $p$, $w$, $\chi$, $\varphi$ and $D$ be as above, with $D$ a lattice family. Let $\mathrm{Lie}$, $W$, $\mathrm{Om}$ and $\mathrm{Om}^{\mathrm{HT}}$ be bundles that belong to $D$. Let $\mathrm{lie}_\tau$ and $\mathrm{om}_\tau$ be local pairs such that, for each $\tau$, $\mathrm{lie}_\tau$ is a flag pair for $(\mathrm{Lie}_\tau, W_\tau)$ and $\mathrm{om}_\tau$ is a flag pair for $(\mathrm{Om}_\tau, \mathrm{Om}^{\mathrm{HT}}_\tau)$, both for $\varpi$ and some bases. Then $\mathrm{lie}$ and $\mathrm{om}$ satisfy the relations at the ideal of the point.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.TopRel.relations` (also `GlobalTheory.T.arithmetic_relations_statement_holds`, a second name).

*Proof.* By the theorem on Chern number relations, the bundles satisfy the Chern number relations. The element $w$ is nonzero: if $w = 0$, then $u p = 0$ with $u$ a unit, so $p = 0$ in $O$, which is false. On each chart the lattices of $\mathrm{Lie}_\tau$ and $W_\tau$ contain each other up to the factors $1$ and $w$, by the base condition of $D$. So $\mathrm{Lie}_\tau$ and $W_\tau$ have the same generic fibre, and in the same way $\mathrm{Om}_\tau$ and $\mathrm{Om}^{\mathrm{HT}}_\tau$ do. A theorem of the development on modules over a uniformizer model then turns the Chern number relations for the bundles into the relations for the flag pairs. $\square$

**Remark 5.5.11 (Formalization).** The proof of `TopRel.relations` builds the equality of generic fibres by hand. The same argument is the lemma `sameGeneric_of` of the descent file, which the proof does not cite. In `stage4` the proof discards the transported annihilator condition, since stage 5 does not need it. In `stage2` it discards the transport of $\mathrm{Good}_2$, which is not yet known on the original model. The refinement in `stage3` comes from a lemma named `lattice_family_model_chern`, whose conclusion is only the line condition. All refinements, transports and the descent lemma are results of the development that the proofs cite.
