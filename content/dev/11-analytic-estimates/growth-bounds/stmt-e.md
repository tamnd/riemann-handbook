---
id: stmt-e
title: Statement E for each datum
kind: theorem
decl: Formalism.MainNotions.TraceSpectra.stmtE
module: Formalism.SharpRestriction.GrowthBounds.AevalValuation
covers: 2159
status: drafted
drafted_by: writer@claude
---
This theorem proves the closed form of Statement E for each datum $D$ of the type `D7`. It proves one valuation bound, `RestChain`, and passes it to [Statement E from the chain bound](/entry/stmt-e-of-chain/). Its only user is [`loc_proved`](/entry/loc-proved/), which makes from it the record `Loc` for [LinkG from local data](/entry/link-of-local-closed/).

## Statement

**Theorem.** For each datum $D$ of the type `D7`, `ClosedFormOfAdmitted D` holds: for all reals $C_\Lambda, C_k, C_{rk}, C_{\deg}$, if `admitted D` $C_\Lambda\, C_k\, C_{rk}\, C_{\deg}$ holds, then there is $C_0 > 0$ such that `aux₃ D C` holds for all $C \ge C_0$.

`admitted` is a conjunction of 37 named conditions on $D$, which we have not unfolded. Only `adm26` reads the four constants.

`aux₃ D C` is a statement about local settings. Let $p \ge 13$ be a natural number. Let $W$ and $O$ be discrete valuation rings with algebras $Q$ and $K$ that are fields, maps $\iota \colon Q \to K$ and $j \colon W \to O$, an automorphism $\sigma$ of $Q$ and an element $w \in O$. Assume that this is an unramified quadratic setting: a Hida setting (not unfolded) with $w$ irreducible, $|O/wO| = p^{2n'}$, and each integer a square in $O$. Let $r \ge 2$, let $T$ be a subset of $\{0, \dots, n'-1\}$, let $\lambda_0 \colon \{0, \dots, n'-1\} \times \{0, \dots, m\} \to \mathbb{Z}$ be a dominant weight with the base weight conditions `WeightHyp`, and let an orbit condition `OrbitHyp` hold. Assume eight numerical inequalities between $C$, $p$, $a$, $Y$, $D_p$ and $c^*$. Then for each integer $t \ge$ `tBound`, `LPprime` holds with $\kappa = C |T| r^2 (m+1) / Y$.

`LPprime` says: for each lattice $L \subset Q^{m+1}$ there are edges $e_1, \dots, e_M$ with target $L$ and vectors $F_i$ in the space `Nsrc` at the source of $e_i$, such that $F_i \in w^{c^*} \mathrm{Re}(e')$ for each other edge $e'$ with the same source, and the family $(F_i)$ has a good rank of at least $(1 - \kappa) \dim V_{\lambda_0}$ (`GoodRankK`). We have not unfolded these four terms.

## Proof

The proof is the term `stmtE_of_chain D restChain`.

`restChain` proves `RestChain` by `restChain_of`, from seven proved facts about the valuation `valS`. For a polynomial $G$ in variables $X_{\ell, c}$ (a letter $\ell$ and a column $c$) and a set $S$ of letters, `valS` substitutes the variables of the letters in $S$ by the action of $g \, \mathrm{diag}(1, \dots, 1, T) \, g^{-1}$ (vector letters) or of its inverse (the other letters), with $g$ the generic matrix, and takes the lowest power of $T$ that appears. The facts `valAeval`, `valFilt` and `valNN` say that `valS` does not drop under suitable substitutions or removal of monomials, and is at least $0$ on vector letters. The facts `phMon`, `compPh`, `fdigPh` and `fdigSum` are rules for the maps `Dt.ph`, `compD` and `Dt.Fdig` on monomials, products and sums.

## In the Lean code

The theorem is at [AevalValuation.lean line 13](lean:Formalism/SharpRestriction/GrowthBounds/AevalValuation.lean#L13), and `restChain` at line 9. `ClosedFormOfAdmitted` is at [TableLineDegreeFive.lean line 244](lean:Formalism/SharpRestriction/GrowthBounds/TableLineDegreeFive.lean#L244) and `aux₃` at line 30.

- The first argument of `aux₃` is written `_D` and is not used. So $D$ enters only through the hypothesis `admitted D`. `second_theorem_absolute_constant` in [PlaneCountTheoremWithConstants.lean line 1137](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1137) relies on this: it gets $C_0$ from one datum $D_0$ and uses it for all $D$.
- `loc_proved` turns this theorem into `SecondTheoremReduced D` by `criterion_restricted_of_closed`, which drops two hypotheses.
- Five Lean files define a `ClosedFormOfAdmitted`. This one is in `tableLineDegreeFive`.
