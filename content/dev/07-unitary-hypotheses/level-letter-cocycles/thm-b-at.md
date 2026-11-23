---
id: thm-b-at
title: Local lifting theorem B at one prime and one pair of fields
kind: theorem
decl: Formalism.MainNotions.N.Ln17.thmB_at
module: Formalism.SharpRestriction.LevelLetterCocycles.FrobeniusStatementOfFontaine
covers: 857
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound of [local lifting theorem B](/entry/theorem-b-closing/) at one prime $\ell$ and one pair $(K, L)$ in case A. [`frobenius_statement_of_inputs`](/entry/frobenius-statement-of-inputs/) calls it at each such triple. The proof is a case split. Each case takes an exponent from a lemma and turns it into a bound on the cokernel length.

## Statement

Use the notation of [local lifting theorem B](/entry/theorem-b-closing/): lattices $T_1, T_2$, a map $F \colon T_1 \to T_2$, integers $b, w, S, \eta, m$, signs $\mathrm{up}(i)$ and sizes $\mathrm{size}(i)$ for $i \in \mathbb{Z}/n$ with $n = [K_0 : \mathbb{Q}_\ell]$, the height $h$, $r = \dim_L T_2$, the band indicator $\beta \in \{0, 1\}$ and the lift exponent $e'$. Write $\lambda$ for the length of $O_L/(\ell)$, $\mathrm{lg} = \log_\ell(2h)$, and

$$\mathrm{Sg} = \frac{h}{\ell^2} + \frac{w + S + \eta}{\ell} + \mathrm{lg} + 1.$$

**Theorem.** Let $C \ge 320$. Assume the records `AdmBoundsB` and `UsedJ` (see [`frobenius_statement_of_inputs`](/entry/frobenius-statement-of-inputs/)). Let $\ell$ be prime and let $(K, L)$ be in case A. Then `ThmB` holds for the Wach module at $(K, L)$ with the constant $C$: under the hypotheses of the theorem, if the signs alternate and no three consecutive letters are thick, then

$$\frac{\mathrm{col}(F)}{\lambda} \le C(n+1)r\Bigl(\frac{h}{\ell^2} + \frac{w + \eta}{\ell} + S + 1 + \mathrm{lg} + \eta\beta\Bigr) + Cnme',$$

and the second bound, with the $R^2$ factors, holds when the signs are constant and no $R$ consecutive letters are thick.

## Proof

Two facts serve every case. First, `adm10` gives a set of at most $(n+1)r$ generators of $H^1_f(T_2)$. Second, the lift condition `coreLiftA` in `adm2` gives: for each finite cocycle $c$ of $T_2$, $\ell^{e'} c$ lies in $\mathrm{Im}(F)$, the image under $F$ of the finite cocycles of $T_1$ plus the coboundaries of $T_2$. The lemma `colLeR_of_exponent` then says: if $Z$ is a finite set of finite cocycles of $T_2$ and $\ell^{e} c \in \mathrm{Im}(F) + \mathrm{span}(Z)$ for every finite cocycle $c$, then

$$\mathrm{col}(F) \le \bigl((n+1)r\,e + |Z|\,e'\bigr)\lambda.$$

1. **Alternating signs, a thick letter, and $b/4 < 40\,\mathrm{Sg}$.** The lemma `exists_liftF_le_sg_of_thick` gives a lift exponent $e_0 \le 160\,\mathrm{Sg}$. Take $Z = \emptyset$ and $e = e_0$.
2. **Alternating signs, the other case.** Either no letter is thick or $40\,\mathrm{Sg} \le b/4$. [`sum_alt`](/entry/sum-alt/) gives $e \le 55\,\mathrm{Sg} + 13S + \eta\beta$ and a set $Z$ with $|Z| \le 4nm$.
3. **Constant signs.** `sum_one` gives $e \le 18\,\mathrm{Sg} + 3R^2(S + 1 + \mathrm{lg}) + 1$ and $|Z| \le (R+1)nm$.

In each case `sg_le_alt` gives $\mathrm{Sg} \le h/\ell^2 + (w+\eta)/\ell + S + 1 + \mathrm{lg}$, and one of `arith_big`, `arith_alt`, `arith_one` checks the inequality of real numbers with $C \ge 320$. The rest is bookkeeping.

## In the Lean code

The theorem is in [FrobeniusStatementOfFontaine.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L119). The lemmas it calls:

- `sum_alt` and `sum_one` in [LogbHBNonneg.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/LogbHBNonneg.lean#L386);
- `exists_liftF_le_sg_of_thick` in [ExistsLiftFLeSgOfThick.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ExistsLiftFLeSgOfThick.lean#L9);
- `colLeR_of_exponent` in [LenQuotSpanNeTopDvr.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/LenQuotSpanNeTopDvr.lean#L57);
- `sg_le_alt`, `arith_alt`, `arith_big`, `arith_one`, `colLeR_mono` and `logb_two_mul_nonneg`, in the same file.

The hypothesis "case A" contains the hypothesis that $L$ is good for $K$, which is also a separate argument. The band indicator is taken with the same constant $C$ as the bound. In case 1 the term $Cnme'$ is not needed: $Z$ is empty.
