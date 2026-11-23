---
title: Good extensions at a bad place
decls:
  - GlobalTheory.LowJoin.exists_good
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good extensions at a bad place

The laws of the last sections are proved place by place. At a bad place of a twisted tower that is not a level place, the local input is a *split place geometry*: a local field, a split point, a uniformiser and an additive character. To apply the local theorems, the geometry must be extended by characters, a system of representatives and coset data, and the extension must agree with the global constants of the tower. This section proves that such a *good* extension exists. The result is used in [the quadratic extension that reads low](/entry/exists-quadratic-extension-reads-low/), where one good extension is chosen at each place of the decoration, for the multiplicity condition in branch 3 of the [unitary hypotheses](/proof/unitary-hypotheses/).

**Setting.** Let $I$ be a valid twisted tower with laws $l$, and let $a$ be an index of the tower. It has a chain of length $m$, a datum of local constants with a level $M$, index data with sets $\beta_j$ and elements $h_j(b, P)$, and characters $\mu^0_j$ and $\xi_a$. Let $P$ be a bad place of $I$ at $a$ that is not a level place. Let $c$ be common see-saw data for the datum of the tower, and $v$ data at the twist places, as before. A *split place geometry* $G$ at $P$ consists of a nonarchimedean local field $k$, a split point $q$ of the host field over $k$, with an embedding $\iota$ of the host field into $k$, a uniformiser $\varpi$, an additive character $\psi_k$ of conductor one, a Haar measure $\nu$ of unit volume, an integer $s$ with $s + 2 = m$, and frames. For characters $\chi_j$ of the ideles, an *extension* $E$ of $G$ for $\chi$ consists of:

- a tame character $\delta$ of $k^\times$ and unramified characters $\eta_j$ of $k^\times$, with $\chi_j^{-1}$ having local component $\eta_{j+1}\delta$ at $q$ for $j \leq s + 1$;
- a family $A_j(d)$ of sets of matrices that is a system of representatives for the local chain datum of $(\delta, \eta)$ and $\psi_k$;
- finite index sets $\mathrm{Ch}_j$, with representatives that are bijections onto $A_j(d)$;
- a level $M$, such that the system is adapted to the boxes of $\varpi^{-M}$ and $\varpi^M$;
- coset representatives of the boxes at the last index, injective and covering up to the orbits of the level group;
- local combinations that represent the test functions of the chain datum in the frames.

The *twist datum* of $E$ is $W(E) = (\varpi, \psi_k, \delta, \eta, \mathrm{sg})$ for a sign $\mathrm{sg}$. A twist datum $W$ is *at twist* for $P$ if the tower has $m = s + 2$ steps, the completion at $P$ is given by $\iota$ and $\varpi$, and $W$ matches the global constants at $P$. That is, $\psi$ agrees with the constant character on the elements made integral by a fixed power of $q_P$, $\delta$ is the inverse of the residue character on units, $(\eta_{i+1}\delta)(\varpi)$ is the constant $\mu_q(i+1, P)$, and the constant square root at $P$ is $\mathrm{sg}\sqrt{q_P}$.

**Definition 2.18.1 (Good extension).** An extension $E$ of $G$ with sign $\mathrm{sg}$ is *good* for $P$ if:

1. $\mathrm{sg} = 1$ or $\mathrm{sg} = -1$;
2. the twist datum $W(E)$ is at twist for $P$;
3. the level of $E$ is the level $M$ of the local constants of the tower;
4. $\mathrm{Ch}_j$ has exactly one element for $j > s + 2$;
5. if $\beta_j$ is not empty, then $A_j(d)$ is the set of matrices $g$ that are the local images of $h_j(b, P)$ for some $b \in \beta_j$;
6. if $\beta_j$ is not empty and $A_{j+1}(d)$ is not empty, then there are an automorphism $\gamma$ at step $j + 1$, bounded at $P$, and an element $b \in \beta_j$, such that the finite sum of large depth of $h_j(b, P)$ and $\gamma$ is not zero.

**Theorem 2.18.2 (Good extensions exist).** Let $I$ be a valid twisted tower, $a$ an index and $P$ a bad place of $I$ at $a$ that is not a level place. Let $G$ be a split place geometry at $P$, let $c$ be valid, and let the global additive character of $c$ be standard of sign $-1$. Let $\chi_j$ be characters with $\chi_j = \mu^0_j\, \xi_a$ for $j < m$, in the sense of equality of characters. Then $\psi_k$ is continuous, and there are an extension $E$ of $G$ for $\chi$ and a sign $\mathrm{sg}$ such that $E$ is good for $P$.

Lean: `GlobalTheory.LowJoin.exists_good`.

*Proof.* We build the twist datum, then a system of representatives, then two extensions.

1. *Preparation.* We have $s + 2 = m$. Since $G$ is a geometry at $P$, the completion at $P$ is given by $\iota$ and $\varpi$, and the idempotent of $G$ is at $P$. The index data of the tower are valid, and $m - 2 = s$.
2. *Local characters.* By the splitting of local Weil characters, applied to the standard character of $c$, every $\chi_{j-1}^{-1}$ has a local component $\mu_j$ at $q$. The character $\psi_k$ is continuous, since it has conductor one. The place $P$ has degree one, by the validity of $I$.
3. *The twist datum.* The theorem on the completion twist data of the chain columns gives a twist datum $W$ at twist for $P$, with $W$ having $\varpi$ and $\psi_k$ as its first entries, $\eta_{i+1}\delta = \mu_{i+1}$ for $i < m$, and sign $\pm 1$. It has two inputs. The first is the formula of the Weil character at a split place of degree one, which gives $\psi_k$ on integral elements as an exponential. The second is the theorem on the local components of the inverse step characters of the chain, which gives that $\mu_{i+1}$ is tame and matches the constants of the tower.
4. *The representatives.* Since $I$ is twisted, the level of the local constants is $m$, so $s + 1 \leq M$. The index data are a product, by the lemma on twist index data. The lemma on the existence of a system then gives a system $A$ of representatives for the chain datum of $W$, adapted to the boxes of $\varpi^{-M}$ and $\varpi^M$, which satisfies items 5 and 6.
5. *The first extension.* By step 3, $\chi_j^{-1}$ has local component $\eta_{j+1}\delta$ for $j \leq s + 1$. The theorem on the extension of a geometry from representatives gives an extension $E_0$ with the characters $\delta, \eta$, the system $A$ and the level $M$.
6. *The second extension.* Choose a representative of each coset of $E_0$ at the last index. These representatives are injective and covering up to orbits, since the cosets of $E_0$ are. The theorem on the extension of a split place geometry from coset orbit representatives gives an extension $E$ with the same $\delta$, $\eta$, $A$ and $M$, and with $\mathrm{Ch}_j$ of one element for $j > s + 2$.
7. *Conclusion.* Item 1 is step 3. The twist datum of $E$ is $(\varpi, \psi_k, \delta, \eta, \mathrm{sg})$, which is $W$, so item 2 holds. Item 3 holds since $E$ has level $M$, item 4 is step 6, and items 5 and 6 are step 4, since $E$ has the system $A$. $\square$

The first extension serves only as a source of coset representatives. The second extension changes the index sets at the top, and keeps all other data of the first.

**Remark 2.18.3 (Formalization).** The theorem is at [TrueGeometryCommutationValue.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TrueGeometryCommutationValue.lean#L79), with the good condition at line 65, the product lemma of step 4 at line 35 and the use in the reading theorem at line 155. The system of step 4 and the continuity of step 2 are in [ContinuousOfCond.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ContinuousOfCond.lean#L90) (lines 90 and 67). The condition at twist is in [EntryAgree.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/EntryAgree.lean#L34), and the geometry and its extensions are in [IsOpenKerUnramMulTame.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsOpenKerUnramMulTame.lean#L121) (the geometry at line 21). The formal proof raises the heartbeat limit to one million. In step 6 it drops the bijection between the new index set and the chosen representatives, which the theorem on coset orbit representatives also gives. We have read the statements, not the proofs, of the splitting of local Weil characters, the completion twist data, the Weil character formula, the local step characters, the lemma on twist index data, the existence of a system and the two extension theorems. We have not unfolded the local chain datum, the systems of representatives, the adapted condition, the boxes and the finite sums of large depth; their descriptions above follow their names and the statements that use them.
